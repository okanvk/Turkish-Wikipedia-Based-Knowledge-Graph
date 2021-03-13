## Turkish-Wikipedia-Based-Knowledge-Graph
This repository includes a Knowledge Graph construction project from Turkish Wikipedia pages. This project constructs a Knowledge Graph from Turkish wikipedia dump, using both the unstructured texts and information boxes. It is developed under inzva AI Projects #6 event, with a group of 4 developers. 

![alt text](https://github.com/okanvk/Turkish-Wikipedia-Based-Knowledge-Graph/blob/main/corpus/1613551272136.jpeg?raw=true)

## Resources that we used
We mainly used two repositories. We constructed a pipeline using both of them in order to construct a knowladge graph. First repository , <a href="https://github.com/informagi/REL"> Radboud Entity Linker</a> which is a modular Entity Linker. 
Second repository is  <a href="https://github.com/theblackcat102/language-models-are-knowledge-graphs-pytorch"> Link </a> which is non-official implementation of the <a href="https://github.com/informagi/REL"> Language Models are Open Knowledge Graphs </a> paper.

# Dia Parser for Dependency Parsing
For dependency parsing, we used  <a href="https://github.com/Unipisa/diaparser"> DiaParser </a>. It didn't have pre-trained parser on Turkish, so we trained new parser using <a href="https://github.com/boun-tabi/UD_Turkish-BOUN"> UD_Turkish-BOUN </a> dataset.
The training dataset contains,
train: 7803 sentences
dev: 979
test: 979
epoch: 304

## Results
It took 1 hours 9 minutes on NVIDIA RTX 2080Ti GPU. We get UAS: 83.2% LAS: 74.83%, on development set. We get UAS: 83.05% LAS: 75.41% on test set. 


# WikiExtractor
This script takes as an input a Wikipedia dump and spits out files such as \
wiki_redirects.txt, \
wiki_name_id_map.txt, \
wiki_disambiguation.txt. 

<a href="https://github.com/informagi/REL/blob/master/scripts/WikiExtractor.py">You can find WikiExtractor script from here.</a>

# Wikipedia2Vec
We used Wikipedia2Vec to obtain page embeddings.
Total number of word occurrences: 457850145
window=5, iteration=10, negative=15
<a href="https://wikipedia2vec.github.io/wikipedia2vec/pretrained/">You can access Wikipedia2Vec official page from here.</a> \
<a href="https://dumps.wikimedia.org/trwiki/20210220/">You can access 2021 Turkish Wikipedia Dump from here.</a> \
<a href="/">DB Dump soon!</a> 



# Lemmatization
We used Zeyrek to apply Lemmatization on words.
<a href="https://github.com/obulat/zeyrek/">You can access from here.</a>

Input: "kedidekiler"
Output: "kedi"


# Adjective, Adverb, Verb Corpus
We used Turkish WordNet and trnlp gihub repository to collect adjective, adverb and verbs.
<a href="https://github.com/StarlangSoftware/TurkishWordNet">You can access Turkish WordNet from here</a>
<a href="https://github.com/StarlangSoftware/TurkishWordNet">You can access trnlp repository from here</a>


## Count based on POS

### Turkish WordNet Count based on POS

|  Adjective Count  |  Adverb Count  | Verb Count | 
|:-----------------:|:--------------:|:----------:|
|     10092         |      2325      |    13274   |   

### trnlp Count based on POS

|  Adjective Count  |  Adverb Count  | Verb Count | 
|:-----------------:|:--------------:|:----------:|
|     8456          |      1416      |    9788    |   


### Total 

|  Adjective Count  |  Adverb Count  | Verb Count | 
|:-----------------:|:--------------:|:----------:|
|     18548         |      3741      |    23062   |   
