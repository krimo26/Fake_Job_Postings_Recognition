# -*- coding: utf-8 -*-
import re


def cleaner(tweet):
    clean_text = tweet

    # normalize the space
    clean_text = re.sub(r"[ ]+", " ", clean_text)
    clean_text = clean_text.strip()
    return clean_text
