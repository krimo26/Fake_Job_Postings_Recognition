# -*- coding: utf-8 -*-

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

 

    

def cleaner(to_clean):
    """convert negative verbs in not"""
    clean_text = to_clean
    ps = PorterStemmer()
    # substitute the negation with a simple "not" tag

    words = word_tokenize(clean_text)
    wordsFiltered = []
     
    for w in words:
        wordsFiltered.append(ps.stem(w))

    clean_text = " ".join(wordsFiltered)
 

    return clean_text
