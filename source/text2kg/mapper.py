from constant import invalid_relations_set

from REL.db.generic import GenericLookup
sqlite_path = "../../../../../media/data/ociftci/Knowledge_Graph/tr_wiki/generated"
emb = GenericLookup("entity_word_embedding", save_dir=sqlite_path, table_name="embeddings")



def Map(head, relations, tail, top_first=True, best_scores = True):
    if head == None or tail == None or relations == None:
        return {}
    head_p_e_m = emb.wiki(str(head), 'wiki')
    if head_p_e_m is None:
        return {}
    tail_p_e_m = emb.wiki(str(tail), 'wiki')
    if tail_p_e_m is None:
        return {}
    
    
    final_tail_p_e_m = tail_p_e_m[0]
    final_head_p_e_m = head_p_e_m[0]
    
    for t_ex in tail_p_e_m:
        if t_ex[0] == "_".join(tail.split()) or t_ex[0].find("_".join(tail.split())) != -1:
            final_tail_p_e_m = t_ex[0]
            break
            
    for h_ex in head_p_e_m:
        if h_ex[0] == "_".join(head.split()) or h_ex[0].find("_".join(head.split())) != -1:
            final_head_p_e_m = h_ex[0]
            break

    

    valid_relations = [ r for r in relations if r not in invalid_relations_set and r.isalpha() and len(r) > 1 ]
    if len(valid_relations) == 0:
        return {}
    return { 'h': final_head_p_e_m[0], 't': final_tail_p_e_m[0], 'r': '_'.join(valid_relations)  }

def deduplication(triplets):
    unique_pairs = []
    pair_confidence = []
    for t in triplets:
        key = '{}\t{}\t{}'.format(t['h'], t['r'], t['t'])
        conf = t['c']
        if key not in unique_pairs:
            unique_pairs.append(key)
            pair_confidence.append(conf)
    
    unique_triplets = []
    for idx, unique_pair in enumerate(unique_pairs):
        h, r, t = unique_pair.split('\t')
        unique_triplets.append({ 'h': h, 'r': r, 't': t , 'c': pair_confidence[idx]})

    return unique_triplets

