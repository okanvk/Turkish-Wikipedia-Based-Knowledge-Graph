import sys

from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

import sparknlp
from sparknlp.annotator import *
from sparknlp.common import *
from sparknlp.base import *
from sparknlp.pretrained import ResourceDownloader
import time
from pathlib import Path
import zeyrek

if sys.version_info[0] < 3:
    from urllib import urlretrieve
else:
    from urllib.request import urlretrieve
    
spark = sparknlp.start()

documentAssembler = DocumentAssembler() \
            .setInputCol("sentence") \
            .setOutputCol("document")

tokenizer = Tokenizer() \
            .setInputCols(["document"]) \
            .setOutputCol("token")

lemmatizer = LemmatizerModel.pretrained("lemma","tr") \
            .setInputCols(["token"]) \
            .setOutputCol("lemma")
finisher = Finisher() \
            .setInputCols([ "lemma"]) \
            .setIncludeMetadata(True)

pipeline_fast_dl = Pipeline(stages = [
            documentAssembler, 
            tokenizer, 
            lemmatizer, 
            finisher])


class TurkishLemmatizer():


    def __init__(self):
	
        self.analyzer = zeyrek.MorphAnalyzer()
        


    def getSparkNlpResult(self,word):
        
        R = Row('sentence')
        data = spark.createDataFrame([R(word)])
        m = self.pipeline_fast_dl.fit(data).transform(data)
        sparkRes = m.select('finished_lemma').collect()[0].finished_lemma
        print(type(sparkRes))
        return sparkRes
        
        
    def bring_lemma(self,word):
        
        
        result_index = 0
        lemma_index_in_tuple = 1
                
        analysis = self.analyzer.lemmatize(word)
        if analysis != None:
            try:
                res = analysis[result_index][lemma_index_in_tuple]
                if len(res) == 0 or len(res) > 1:
                    return self.getSparkNlpResult(word)
                return res
            except IndexError:
                return self.getSparkNlpResult(word)
        return self.getSparkNlpResult(word)

a = TurkishLemmatizer()
print(a.bring_lemma("gözlükler"))
