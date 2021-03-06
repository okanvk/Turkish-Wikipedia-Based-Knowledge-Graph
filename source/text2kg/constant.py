found_invalid = ["ve","veya","ki","ni"]

invalid_relations = ["of"] + found_invalid

auxiliaries = ["of"]

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
