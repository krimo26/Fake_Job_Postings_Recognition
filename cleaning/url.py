# -*- coding: utf-8 -*-
import re


def cleaner(tweet):
    """ remove urls and mentions """
    clean_text = tweet

    clean_text = clean_text.replace("\t", " ").replace("\n", " ")

    # remove the url
    clean_text = re.sub(r"(http|https):\S+", " ", clean_text)
    clean_text = re.sub("www\S+", " ", clean_text)

    # remove the url of twitter's pic
    clean_text = re.sub(r"pic.twitter.com\S+", " ", clean_text)


    # remove the @ (mentions)
    clean_text = re.sub(r"@\S+", " ", clean_text)

    # remove the RT
    clean_text = re.sub(r"(RT )", " ", clean_text)

    return clean_text
