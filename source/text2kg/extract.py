
import sys, os
from process import parse_sentence
from mapper import Map, deduplication
from transformers import AutoTokenizer, BertModel
import argparse
from tqdm import tqdm
import json
from doc import Doc
from turkish_lemma import TurkishLemmatizer


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description='Process lines of text corpus into knowledgraph')
parser.add_argument('input_filename', type=str, help='text file as input')
parser.add_argument('output_filename', type=str, help='output text file')
parser.add_argument('--language_model',default='dbmdz/bert-base-turkish-cased', 
                    choices=[ 'dbmdz/bert-base-turkish-cased', 'bert-base-turkish-uncased'],
                    help='which language model to use')
parser.add_argument('--use_cuda', default=True, 
                        type=str2bool, nargs='?',
                        help="Use cuda?")
parser.add_argument('--include_text_output', default=False, 
                        type=str2bool, nargs='?',
                        help="Include original sentence in output")
parser.add_argument('--threshold', default=0.003, 
                        type=float, help="Any attention score lower than this is removed")

args = parser.parse_args()

use_cuda = args.use_cuda
lemmatizer = TurkishLemmatizer()
language_model = args.language_model


if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained(language_model)
    encoder = BertModel.from_pretrained(language_model)
    encoder.eval()
    if use_cuda:
        encoder = encoder.cuda()    
    input_filename = args.input_filename
    output_filename = args.output_filename
    include_sentence = args.include_text_output

    with open(input_filename, 'r') as f, open(output_filename, 'w') as g:
        for idx, line in enumerate(tqdm(f)):
            sentence  = line.strip()
            if len(sentence):
                valid_triplets = []
                doc = Doc()
                for sent in doc.sentence_tokenization(sentence):
                    # Match
                    for triplets in parse_sentence(sent, tokenizer, encoder, lemmatizer, use_cuda=use_cuda):
                        valid_triplets.append(triplets)
                if len(valid_triplets) > 0:
                    # Map
                    mapped_triplets = []
                    for triplet in valid_triplets:
                        head = triplet['h']
                        tail = triplet['t']
                        relations = triplet['r']
                        conf = triplet['c']
                        if conf < args.threshold:
                            continue
                        mapped_triplet = Map(head, relations, tail)
                        if 'h' in mapped_triplet:
                            mapped_triplet['c'] = conf
                            mapped_triplets.append(mapped_triplet)
                    output = { 'line': idx, 'tri': deduplication(mapped_triplets) }

                    if include_sentence:
                        output['sent'] = sentence
                    if len(output['tri']) > 0:
                        g.write(json.dumps( output )+'\n')
