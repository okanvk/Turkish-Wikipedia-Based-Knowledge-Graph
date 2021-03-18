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

class TurkishLemmatizer():


    def __init__(self):
        self.analyzer = zeyrek.MorphAnalyzer()
        
        self.documentAssembler = DocumentAssembler() \
            .setInputCol("sentence") \
            .setOutputCol("document")

        self.tokenizer = Tokenizer() \
            .setInputCols(["document"]) \
            .setOutputCol("token")

        self.lemmatizer = LemmatizerModel.pretrained("lemma","tr") \
            .setInputCols(["token"]) \
            .setOutputCol("lemma")

        self.finisher = Finisher() \
            .setInputCols([ "lemma"]) \
            .setIncludeMetadata(True)

        self.pipeline_fast_dl = Pipeline(stages = [
            self.documentAssembler, 
            self.tokenizer, 
            self.lemmatizer, 
            self.finisher])
        
    def bring_lemma(self,word):
        
        R = Row('sentence')    
        
        result_index = 0
        lemma_index_in_tuple = 1
                
        analysis = self.analyzer.lemmatize(word)
        if analysis != None:
            try:
                res = analysis[result_index][lemma_index_in_tuple]
                if len(res) == 0:
                    data = spark.createDataFrame([R(word)])
                    m = self.pipeline_fast_dl.fit(data).transform(data)
                    sparkRes = m.select('sentence').collect()[0].sentence
                    return [sparkRes]
                return res
            except IndexError:
                data = spark.createDataFrame([R(word)])
                m = self.pipeline_fast_dl.fit(data).transform(data)
                sparkRes = m.select('sentence').collect()[0].sentence
                return [sparkRes]
        data = spark.createDataFrame([R(word)])
        m = self.pipeline_fast_dl.fit(data).transform(data)
        sparkRes = m.select('sentence').collect()[0].sentence
        return [sparkRes]

