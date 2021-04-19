from nltk.tokenize import word_tokenize,sent_tokenize
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
from transformers import PretrainedConfig
import re
from transformers import TokenClassificationPipeline
import spacy



class Doc:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Alaeddin/convbert-base-turkish-ner-cased")
        self.model = AutoModelForTokenClassification.from_pretrained("Alaeddin/convbert-base-turkish-ner-cased")
        self.config = PretrainedConfig.from_pretrained("Alaeddin/convbert-base-turkish-ner-cased")
        self.pipeline = pipeline('ner', model=model, tokenizer=tokenizer, config=config)
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp_grouped = TokenClassificationPipeline(
            model=model,
            tokenizer=tokenizer,
            grouped_entities=True
        )

    def _bringNers(self,res,score_threshold = 0.95):
        ner_chunks = []
        for item in res:
            if item["score"] > score_threshold:
                ner_chunks.append(item["word"])
        return ner_chunks

    def _bringChunks(self,doc,ners):
        ner_chunks = []
        start_chunks = []
        end_chunks = []
        token_dict = {}

        for ner in ners:
          ner_chunks.append(ner)
          ner_doc = self.nlp(ner)  
          tokens = []
       
          for token in ner_doc:
            tokens.append(token.text)
            if token.text in token_dict.keys():
              token_dict[token.text] += 1
            else:
              token_dict[token.text] = 1
            
          ner_len = len(tokens)
          state = True
          i = 0
          doc_dict = {}

          for idx, token in enumerate(doc):

            if token.text in doc_dict.keys():
              doc_dict[token.text] += 1
            else:
              doc_dict[token.text] = 1

            if i == len(tokens):
              end_chunks.append(idx)
              break

            if token.text == tokens[i] and doc_dict[token.text] == token_dict[token.text]:
                if state:
                  start_chunks.append(idx)
                  state = False
                i += 1
        return start_chunks,end_chunks,ner_chunks


    def _get_index(self,doc,start_chunk,end_chunk,ner_chunks):
        sentence_mapping = []
        token2id = {}
        mode = 0 # 1 in chunk, 0 not in chunk
        chunk_id = 0

        for idx, token in enumerate(doc):
            if idx in start_chunk:
                mode = 1
                sentence_mapping.append(ner_chunks[chunk_id])
                token2id[sentence_mapping[-1]] = len(token2id)
                chunk_id += 1
            elif idx in end_chunk:
                mode = 0

            if mode == 0:
                sentence_mapping.append(token.text)
                token2id[sentence_mapping[-1]] = len(token2id)
       return sentece_mapping,token2id



    def find_ner_tags(self,sentence):
        
        sentence = re.sub(r"'\w+|’\w+", '', sentence)
        doc = self.nlp(sentence)
        res = nlp_grouped(sentence)   
        ners = self._bringNers(res)        
        start_chunk,end_chunk,ner_chunks = self._bringChunks(doc,ners) 
        sentence_mapping,token2id = self.get_index(doc,start_chunk,end_chunk,ner_chunks)
        return sentence_mapping, token2id, ner_chunks


    
    def sentence_tokenization(self,paragraph):
        return sent_tokenize(paragraph)

    
    def word_tokenization(self,sent):
        return word_tokenize(sent)


