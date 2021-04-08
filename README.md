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

```
from wikipedia2vec import Wikipedia2Vec
wiki2vec = Wikipedia2Vec.load('wikipedia2vec_trained')
wiki2vec.most_similar(wiki2vec.get_entity('Atatürk'), 5)

>>> [(<Entity Mustafa Kemal Atatürk>, 0.9999999), (<Word atatürk>, 0.9274426), (<Word kemal>, 0.782923), (<Entity Kategori:Mustafa Kemal Atatürk>, 0.77045125), (<Entity Yardım:Açıklamalı sayfa>, 0.7423448)]

```

```
wiki2vec.most_similar(wiki2vec.get_entity('Fatih Terim'), 5)

>>> [(<Entity Fatih Terim>, 1.0), (<Entity Şenol Güneş>, 0.7102364), (<Entity Müfit Erkasap>, 0.6819058), (<Entity Abdullah Avcı>, 0.67471796), (<Word hiddink>, 0.6672677)]

```
We used Wikipedia2Vec to obtain page embeddings. \
Total number of word occurrences: 457850145 \
Hyperparameters: window=5, iteration=10, negative=15 

<a href="https://wikipedia2vec.github.io/wikipedia2vec/pretrained/">You can access Wikipedia2Vec official page from here.</a> \
<a href="https://dumps.wikimedia.org/trwiki/20210220/">You can access 2021 Turkish Wikipedia Dump from here.</a> \
<a href="/">Binary file soon!</a> 

# NER
We trained a Named Entity Recognition which is trained with <a href="https://huggingface.co/dbmdz/convbert-base-turkish-cased"> Convberturk </a> language model

## Model Parameters
Batch size : 32 \
Epoch : 5 \
Maximum sequence length : 512

## Dataset
We used <a href="https://arxiv.org/abs/2003.11080"> Xtreme Dataset</a> in order to train, test and validate our model.
We trained convbert model with merging train and extra files and we got the results on validation file. 

## Results
The results are shown below

|  Precision |  Recall  | F1 | loss |
|:-----------------:|:--------------:|:----------:|:----------:|
|     95.83         |      96.84      |    96.33   |   0.0665


## Model link
You can access our convbert Named Entity Recognition model from <a href="https://huggingface.co/Alaeddin/convbert-base-turkish-ner-cased"> here </a>

# Lemmatization
We used the combination of <a href="https://github.com/obulat/zeyrek/">Zeyrek</a>  and <a href="https://github.com/akoksal/Turkish-Lemmatizer">Turkish lemmatizer </a> to apply Lemmatization on words.


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
