# -*- coding: utf-8 -*-
import re


def cleaner(tweet):
    """convert negative verbs in not"""
    clean_text = tweet

    # substitute the negation with a simple "not" tag

    clean_text = re.sub(r"isn't", " not ", clean_text)
    clean_text = re.sub(r"aren't", " not ", clean_text)
    clean_text = re.sub(r"don't", " not ", clean_text)
    clean_text = re.sub(r"didn't", " not ", clean_text)
    clean_text = re.sub(r"doesn't", " not ", clean_text)
    clean_text = re.sub(r"haven't", " not ", clean_text)
    clean_text = re.sub(r"hasn't", " not ", clean_text)
    clean_text = re.sub(r"wasn't", " not ", clean_text)
    clean_text = re.sub(r"weren't", " not ", clean_text)
    clean_text = re.sub(r"won't", " not ", clean_text)
    clean_text = re.sub(r"never", " not ", clean_text)
    clean_text = re.sub(r"can't", " not ", clean_text)
    clean_text = re.sub(r"cannot", " not ", clean_text)
    clean_text = re.sub(r"couldn't", " not ", clean_text)
    clean_text = re.sub(r"wouldn't", " not ", clean_text)
    clean_text = re.sub(r"shouldn't", " not ", clean_text)
    clean_text = re.sub(r"mustn't", " not ", clean_text)
    clean_text = re.sub(r"needn't", " not ", clean_text)

    # same negation without quote
    clean_text = re.sub(r" isnt ", " not ", clean_text)
    clean_text = re.sub(r" arent ", " not ", clean_text)
    clean_text = re.sub(r" dont ", " not ", clean_text)
    clean_text = re.sub(r" didnt ", " not ", clean_text)
    clean_text = re.sub(r" doesnt ", " not ", clean_text)
    clean_text = re.sub(r" havent ", " not ", clean_text)
    clean_text = re.sub(r" hasnt ", " not ", clean_text)
    clean_text = re.sub(r" wasnt ", " not ", clean_text)
    clean_text = re.sub(r" werent ", " not ", clean_text)
    clean_text = re.sub(r" wont ", " not ", clean_text)
    clean_text = re.sub(r" cant ", " not ", clean_text)
    clean_text = re.sub(r" couldnt ", " not ", clean_text)
    clean_text = re.sub(r" wouldnt ", " not ", clean_text)
    clean_text = re.sub(r" shouldnt ", " not ", clean_text)
    clean_text = re.sub(r" mustnt ", " not ", clean_text)
    clean_text = re.sub(r" neednt ", " not ", clean_text)

    clean_text = re.sub(r"Isn't", " not ", clean_text)
    clean_text = re.sub(r"Aren't", " not ", clean_text)
    clean_text = re.sub(r"Don't", " not ", clean_text)
    clean_text = re.sub(r"Didn't", " not ", clean_text)
    clean_text = re.sub(r"Doesn't", " not ", clean_text)
    clean_text = re.sub(r"Haven't", " not ", clean_text)
    clean_text = re.sub(r"Hasn't", " not ", clean_text)
    clean_text = re.sub(r"Wasn't", " not ", clean_text)
    clean_text = re.sub(r"Weren't", " not ", clean_text)
    clean_text = re.sub(r"Won't", " not ", clean_text)
    clean_text = re.sub(r"Never", " not ", clean_text)
    clean_text = re.sub(r"Can't", " not ", clean_text)
    clean_text = re.sub(r"Cannot", " not ", clean_text)
    clean_text = re.sub(r"Couldn't", " not ", clean_text)
    clean_text = re.sub(r"Wouldn't", " not ", clean_text)
    clean_text = re.sub(r"Shouldn't", " not ", clean_text)
    clean_text = re.sub(r"Mustn't", " not ", clean_text)
    clean_text = re.sub(r"Needn't", " not ", clean_text)
    clean_text = re.sub(r" Ain't ", " not ", clean_text)

    return clean_text
