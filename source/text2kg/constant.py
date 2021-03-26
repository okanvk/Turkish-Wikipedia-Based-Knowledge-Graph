found_invalid = ["ve","veya","ki","de","da","ni","ile", "bat", "Aram", "Sosyo", "ev", "kat", "ad",  "ilgi", "is", "edi", "bağ", "acaba", "ama", "az", "aslında",
"bazı",
"belki",
"beri",
"biri",
"birkaç",
"birşey",
"biz",
"bu",
"çok",
"çünkü",
"da",
"daha",
"dan",
"de",
"den",
"defa",
"diye",
"eğer",
"en",
"gibi",
"hem",
"hep",
"hepsi",
"her",
"hiç",
"için",
"ise",
"kez",
"ki",
"kim",
"kilo",
"metre",
"mı",
"mu",
"mü",
"nasıl",
"ne",
"neden",
"nerde",
"nerede",
"nereye",
"niçin",
"niye",
"o",
"sanki",
"şey",
"siz",
"şu",
"tüm",
"ya",
"yani",
"!",
"?",
"bir",
"iki",
"üç",
"dört",
"beş",
"altı",
"yedi",
"sekiz",
"dokuz",
"on"]

invalid_relations = [] + found_invalid

auxiliaries = ["olmak", "ol", "etmek", "et", "demek", "de"]

with open('../../corpus/trnlp-data/tr_adj.txt', 'r') as f:
    adjectives_trnlp = [ line.strip().lower() for line in f]

with open('../../corpus/trnlp-data/tr_adverb.txt', 'r') as f:
    adverbs_trnlp = [ line.strip().lower() for line in f]

with open('../../corpus/wordnet-data/tr_adjectives.txt', 'r') as f:
    adjectives_wordnet = [ line.strip().lower() for line in f]

with open('../../corpus/wordnet-data/tr_adverbs.txt', 'r') as f:
    adverbs_wordnet = [ line.strip().lower() for line in f]


# with open('corpus/Wordlist-Verbs-All.txt', 'r') as f:
#     verbs = [ line.strip().lower() for line in f]

invalid_relations += adverbs_wordnet
invalid_relations += adverbs_trnlp
invalid_relations += adjectives_wordnet
invalid_relations += adjectives_trnlp

# invalid_relations += verbs

invalid_relations_set = set(invalid_relations)

