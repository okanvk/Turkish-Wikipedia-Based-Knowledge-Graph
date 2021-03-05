from nltk.tokenize import word_tokenize,sent_tokenize
from transformers import pipeline,AutoModelForTokenClassification,AutoTokenizer, AutoModel



class Doc:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("mustafabaris/tr_kg_pos_conllu_bert")
        self.model = AutoModelForTokenClassification.from_pretrained("mustafabaris/tr_kg_pos_conllu_bert")
        self.pipeline = pipeline('ner', model=self.model, tokenizer=self.tokenizer)

    def get_chunk(self,res,start,end):
        return " ".join([res[i]["word"] for i in range(start,end)])


    def get_index(self,res,start_chunk,end_chunk,noun_chunks):
        sentence_mapping = []
        token2id = {}
        mode = 0 # 1 in chunk, 0 not in chunk
        chunk_id = 0

        for idx in range(len(res)):
            token = res[idx]["word"]
            if idx in start_chunk:
                mode = 1
                sentence_mapping.append(noun_chunks[chunk_id])
                token2id[sentence_mapping[-1]] = len(token2id) 
                chunk_id += 1
            elif idx in end_chunk:
                mode = 0
            if mode == 0:
                sentence_mapping.append(token)
                token2id[sentence_mapping[-1]] = len(token2id)
        return sentence_mapping,token2id

    def find_chunk(self,sentence,model,tokenizer):
        start_chunk = []
        end_chunk = []
        noun_chunks = []
        is_noun = False

        for i in range(len(res)):
            if res[i]["entity"] == "NOUN" or res[i]["entity"] == "PROPN":
                if not is_noun:
                    start_chunk.append(i)
                    is_noun = True
            else:
                if is_noun:
                    end_chunk.append(i)
                    is_noun = False

        noun_chunks = [self.get_chunk(res,start_chunk[i],end_chunk[i]) for i in range(len(start_chunk))]
        return start_chunk,end_chunk,noun_chunks

    def find_pos_tags(self,sent):
        res = self.pipeline(sentence)
        start_chunk,end_chunk,noun_chunks = self.find_chunk(res,self.model,self.tokenizer)
        return sentence_mapping,token2id = self.get_index(res,start_chunk,end_chunk,noun_chunks)


    def sentence_tokenization(self,paragraph):
        return sent_tokenize(paragraph)

    
    def word_tokenization(self,sent):
        return word_tokenize(sent)

doc = Doc()
