## Turkish-Wikipedia-Based-Knowledge-Graph



# Wikipedia2Vec
We used Wikipedia2Vec to obtain page embeddings.
Total number of word occurrences: 457850145
window=5, iteration=10, negative=15
<a href="https://wikipedia2vec.github.io/wikipedia2vec/pretrained/">You can access Wikipedia2Vec official page from here</a>
<a href="https://dumps.wikimedia.org/trwiki/20210220/">You can access 2021 Turkish Wikipedia Dump from here</a>
<a href="/">DB Dump soon!</a>



# Lemmatization
We used Zeyrek to apply Lemmatization on words.
<a href="https://github.com/obulat/zeyrek/">You can access from here</a>

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
