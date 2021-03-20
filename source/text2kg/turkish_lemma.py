
import zeyrek
import stanza

stanza.download('tr')

class TurkishLemmatizer():


    def __init__(self):
        self.analyzer = zeyrek.MorphAnalyzer()
        self.nlp = stanza.Pipeline(lang='tr', processors='tokenize,lemma',use_gpu=False)

    def _bringStanzaLemma(self,word):
        doc = self.nlp(word)
        first_lemma = [word.lemma for sent in doc.sentences for word in sent.words][0]
        return [first_lemma]

    def bring_lemma(self,word):
        result_index = 0
        lemma_index_in_tuple = 1
        try:
            res = self.analyzer.analyze(word)[result_index][lemma_index_in_tuple]
            if len(res) == 0 or len(res) >= 1:
               return self._bringStanzaLemma(word)
            return res
        except IndexError:
            return self._bringStanzaLemma(word)
        return self._bringStanzaLemma(word)

