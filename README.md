## Turkish-Wikipedia-Based-Knowledge-Graph
This repository includes a Knowledge Graph construction project from Turkish Wikipedia pages. This project constructs a Knowledge Graph from Turkish wikipedia dump, using both the unstructured texts and information boxes. It is developed under inzva AI Projects #6 event, with a group of 4 developers. 

![alt text](https://github.com/okanvk/Turkish-Wikipedia-Based-Knowledge-Graph/blob/main/img/ai6.jpeg?raw=true)

## Resources that we used
We mainly used two repositories. We constructed a pipeline using both of them in order to construct a knowledge graph. First repository , <a href="https://github.com/informagi/REL"> Radboud Entity Linker</a> which is a modular Entity Linker. 
Second repository is  <a href="https://github.com/theblackcat102/language-models-are-knowledge-graphs-pytorch"> Link </a> which is non-official implementation of the <a href="https://github.com/informagi/REL"> Language Models are Open Knowledge Graphs </a> paper.

# Dia Parser for Dependency Parsing
For dependency parsing, we used  <a href="https://github.com/Unipisa/diaparser"> DiaParser </a>. It didn't have pre-trained parser on Turkish, so we trained new parser using <a href="https://github.com/boun-tabi/UD_Turkish-BOUN"> UD_Turkish-BOUN </a> dataset.
The training dataset contains 7803 sentences for training 979 sentences for development 979 sentences for testing.
## Results

|               Model                 |  UAS on Dev    |  LAS on Dev  | UAS on Test | LAS on Test | 
|:-----------------------------------:|:--------------:|:----------:|:-----------:|:-------------:|
| bert-base-turkish-cased             |      83.20%    |   74.83%   |   83.05%    |     75.41%    |
| electra-base-turkish-discriminator  |      84.09%    |   75.50%   |   84.04%    |     76.06%    |
| convbert-base-turkish-cased         |      83.12%    |   74.86%   |   82.55%    |     75.21%    |


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
We used the combination of <a href="https://github.com/obulat/zeyrek/">Zeyrek</a>  and <a href="https://stanfordnlp.github.io/stanza/lemma.html">Turkish lemmatizer in stanza</a> to apply Lemmatization on words.

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
