import zeyrek
from lemmatizer import bring_first_lemma

class TurkishLemmatizer():
    def __init__(self):
        self.analyzer = zeyrek.MorphAnalyzer()

    def bring_lemma(self,word):
        result_index = 0
        lemma_index_in_tuple = 1
        try:
            res = self.analyzer.analyze(word)[result_index][lemma_index_in_tuple]
            if len(res) == 0 or len(res) >= 1:
               return self.bring_first_lemma(word)
            return res
        except IndexError:
            return self.bring_first_lemma(word)
        return self.bring_first_lemma(word)

