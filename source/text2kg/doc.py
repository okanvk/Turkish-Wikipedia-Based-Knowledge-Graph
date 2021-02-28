from nltk.tokenize import word_tokenize,sent_tokenize
from transformers import AutoTokenizer, AutoModel



class Doc:

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("mustafabaris/tr_kg_pos_conllu_bert")
        self.model = AutoModel.from_pretrained("mustafabaris/tr_kg_pos_conllu_bert")
        self.pipeline = pipeline('pos', model=self.model, tokenizer=self.tokenizer)


    def find_pos_tags(sent):
        res = self.pipeline(sent)
        print(res)


    def sentence_tokenization(self,paragraph):
        return sent_tokenize(paragraph)

    
    def word_tokenization(self,sent):
        return word_tokenize(sent)