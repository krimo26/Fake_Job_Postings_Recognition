# -*- coding: utf-8 -*-
import re


def cleaner(tweet):
    """ remove punctuation """
    clean_text = tweet

    # Prima di rimuovere la punteggiatura cerco le espressioni multiple
    clean_text = re.sub(r"!!+", " multiExclamation ", clean_text)
    clean_text = re.sub(r"\?\?+", " multiInterrogation ", clean_text)
    clean_text = re.sub(r"(\?!)+", " multiSurprise ", clean_text)
    clean_text = re.sub(r"(!\?)+", " multiSurprise ", clean_text)
    clean_text = re.sub(r"\.\.+", " multiPoint ", clean_text)

    # remove the punctuation except for "." and ","
    clean_text = re.sub(r":|;|\?|!|'", " ", clean_text)
    clean_text = re.sub(r"&", "and", clean_text)

    # remove "." and "," only if not among numbers
    # \D is any character except for the cipher

    clean_text = re.sub(r'(?P<first>\D)(\.)(?P<second>\D)', r'\g<first> \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>\D)(,)(?P<second>\D)', r'\g<first> \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>\D)(\.)(?P<second>\D)', r'\g<first> \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>\D)(,)(?P<second>\D)', r'\g<first> \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>.)(\.) ', r'\g<first> ', clean_text)
    clean_text = re.sub('\.\n', " ", clean_text)        # il punto è prima di un a capo
    clean_text = re.sub('\.$', " ", clean_text)         # il punto è alla fine della stringa
    clean_text = re.sub('^( )*\.', " ", clean_text)     # il punto è il primo carattere della stringa

    return clean_text