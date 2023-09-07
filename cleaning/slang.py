# -*- coding: utf-8 -*-
import re
from nltk.tokenize import TweetTokenizer


def cleaner(tweet):
    """convert slang in common words"""
    text = " " + tweet + " "
    t2 = TweetTokenizer()

    f = open("acronyms.txt", "r")
    while 1:
        line = f.readline()
        if line == "":
            break

        token = t2.tokenize(line)
        text = re.sub(" " + token[0] + " ", " " + token[1] + " ", text)
        text = re.sub(" gotta ", ' got to ', text)
        text = re.sub(" let's ", ' let us ', text)
        text = re.sub(" c'mon ", ' come on ', text)
        text = re.sub("Let's ", ' let us ', text)
        text = re.sub("C'mon ", ' come on ', text)

    f.close()

    return text
