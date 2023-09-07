# -*- coding: utf-8 -*-
import re


def cleaner(to_clean):
    """convert negative verbs in not"""
    clean_text = to_clean

    # substitute the negation with a simple "not" tag

    clean_text = re.sub(r"'d ", " would ", clean_text)
    clean_text = re.sub(r"'re ", " are ", clean_text)
    clean_text = re.sub(r"'ve ", " have ", clean_text)
    clean_text = re.sub(" I'm ", " I am ", clean_text)
    clean_text = re.sub("'ll ", " will ", clean_text)
    clean_text = re.sub(" it's ", " it is ", clean_text)
    clean_text = re.sub("It's ", " It is ", clean_text)
    clean_text = re.sub(" that's ", " that is ", clean_text)
    clean_text = re.sub("That's ", " That is ", clean_text)
    clean_text = re.sub(" what's ", " what is ", clean_text)
    clean_text = re.sub("What's ", " What is ", clean_text)

    return clean_text
