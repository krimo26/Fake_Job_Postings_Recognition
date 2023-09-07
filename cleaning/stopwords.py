# -*- coding: utf-8 -*-
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def cleaner(to_clean):
    """convert negative verbs in not"""
    clean_text = to_clean

    # substitute the negation with a simple "not" tag

    stopWords = set(stopwords.words('english'))
    words = word_tokenize(clean_text)
    wordsFiltered = []
     
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    clean_text = " ".join(wordsFiltered)
 

    return clean_text
