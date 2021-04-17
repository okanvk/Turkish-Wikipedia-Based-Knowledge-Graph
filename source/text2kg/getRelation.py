import unicodedata
from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote

def check_blank(text):
    if text.startswith('\n'):
        text = text[1:]
    if text.endswith('\n'):
        text = text[:-1]
    return text



def preProcess(string):
    return unicodedata.normalize("NFKD",string)


def getInfoBox(pageName):

    url = requests.get("https://tr.wikipedia.org/wiki/"+pageName).text
    soup = BeautifulSoup(url,'html.parser')
    result = {}
    exceptional_row_count = 0
    for infoBox in ["infobox vcard","infobox vcard plainlist",'infobox biography vcard','infobox geography vcard','infobox vevent']:
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
    index = 1
    unique = set()
    try:
        for key in data.keys():
            for value in data[key]:
                if len(value) != 0:
                    temp = {'line':index}
                    t = ''
                    
                    if 'link' in value.keys():
                        t = value['link'].lower()
                    else:
                        t = value['name'].lower()
                    
                    if len(t) > 0:
                        temp_r = key.lower().replace(' ','_')
                        temp_unique = temp_r+t
                        if temp_unique not in unique:
                            unique.add(temp_unique)
                            temp['tri']= [{'h':pageName,'t':t,'r':temp_r,'c':1}]
                        
                if len(list(temp.keys())) > 1 :
                    result.append(temp)
                    index += 1
    except:
        return []

    if len(result) == 0:
        return []
    return result

print(getRelation(getInfoBox("Taran"),'Tarkan'))
