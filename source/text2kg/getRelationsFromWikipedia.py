
import unicodedata
from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote
import re

def check_blank(text):
    if text.startswith('\n'):
        text = text[1:]
    if text.endswith('\n'):
        text = text[:-1]
    return text

def clear_tail(text):
  searched = "/wiki/"
  start_index = text.find(searched)
  if start_index != -1:
     removed_wiki_chunk = text[start_index+len(searched):]
     if removed_wiki_chunk.find("_") != -1:
       tokens = removed_wiki_chunk.split("_")
       capitalized_tokens = [t.capitalize() for t in tokens]
       return "_".join(capitalized_tokens)
     else:
       return removed_wiki_chunk
  else:
    return text

def preProcess(string):
    return unicodedata.normalize("NFKD",string)

def getInfoBox(pageName):

    url = requests.get("https://tr.wikipedia.org/wiki/"+pageName).text
    soup = BeautifulSoup(url,'html.parser')
    result = {}
    exceptional_row_count = 0
    for infoBox in ["infobox vcard","infobox vcard plainlist",'infobox biography vcard','infobox geography vcard','infobox vevent','infobox']:
        table = soup.find('table', class_=infoBox)
        if table is None:
            continue
        parent = ""
        for tr in table.find_all('tr'):
            try:
                if tr.find('th'):
                    tr_temp = tr.find('th').text
                    tr_temp = preProcess(unquote(check_blank(tr_temp)))
                    if not tr_temp in result.keys():
                        result[tr_temp] = []
                    for a in tr.find('td').find_all('a'):
                        result[tr_temp].append({'name':preProcess(unquote(check_blank(a.text))),'link':unquote(a['href'])})

                    for span in tr.find('td').find_all('span'):
                        if span.find('b'):
                            result[tr_temp].append({'name':preProcess(unquote(check_blank(span.find('b').text)))})
                        else:
                            result[tr_temp].append({'name':preProcess(unquote(check_blank(span.text)))})
                    for plainText in tr.find('td'):
                        result[tr_temp].append({'name':preProcess(unquote(check_blank(plainText)))})
                else:
                    exceptional_row_count += 1
            except:
                exceptional_row_count += 1 	
    return result

def getRelation(data,pageName):
    result = []
    unique = set()
    title_tag = "title="
    action_http = "&action"
    try:
        for key in data.keys():
            for value in data[key]:
                if len(value) != 0:
                    temp = {'line': pageName}
                    t = ''
                    if 'link' in value.keys():
                        t = value['link'].lower()
                    else:
                        t = value['name'].lower()
                    if len(t) > 0:
                        temp_r = key.lower().replace(' ','_')

                        if temp_r.isspace() or t.find("#") != -1 or t.isspace() or t.find("https") != -1 or t.find("svg") != -1:
                          continue
                        
                        if t.find("index.php") != -1 and t.find(title_tag) != -1 and t.find(action_http) != -1:
                          t = t[t.find(title_tag) + len(title_tag) :t.find(action_http)]

                        temp_r = temp_r.replace("("," ")
                        temp_r = temp_r.replace(")"," ")
                        temp_r = re.sub(' +', ' ', temp_r)

                        temp_unique = temp_r+t
                        if temp_unique not in unique:
                            clean_tail = clear_tail(t)
                            unique.add(temp_unique)
                            temp['tri']= [{'h':pageName,'t':clean_tail,'r':temp_r,'c':1}]  

                if len(list(temp.keys())) > 1 :
                    result.append(temp)
    except:
        return {"line" : pageName, "tri" : []}

    if len(result) == 0:
        return {"line" : pageName, "tri" : []}
    
    triplets = []
    for res in result:
      response_triplets = res["tri"]
      for triplet in response_triplets:
        triplets.append(triplet)
    output = {"line" : pageName, "tri" : triplets}
    return output
