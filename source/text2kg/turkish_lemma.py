import zeyrek
class TurkishLemmatizer():


    def __init__(self):
        self.analyzer = zeyrek.MorphAnalyzer()


    def bring_lemma(self,word):
        result_index = 0
        lemma_index_in_tuple = 1
        try:
            res = analysis[result_index][lemma_index_in_tuple]
            if len(res) == 0:
                return [word]
            return res
        except IndexError:
            return [word]
        return [word]
