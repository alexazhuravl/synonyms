import pandas as pd
from nltk.corpus import wordnet as wn
import json


def synonimize(w):
    data = []
    for ss in wn.synsets(w):
        data += [ss.lemma_names()]
    flat_list = [item for sublist in data for item in sublist]
    data_unique = list(set(flat_list))
    return data_unique


if __name__ == '__main__':

    df = pd.read_csv('./data.csv')
    d = pd.Series(df.KEY_WORD.values, index=df.BODY_FUNCTION).to_dict()
    syn_data = []
    for key, value in d.items():
        vals = {'body_function': key.lower(), 'key_word': value.lower(),
                'synonyms': (synonimize(value.lower()))}
        syn_data += [vals]

    res = json.dumps(syn_data)
