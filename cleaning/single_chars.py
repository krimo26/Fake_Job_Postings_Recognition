# -*- coding: utf-8 -*-
import re
import string


def cleaner(tweet):
    # elimina i caratteri alfabetici singoli, solo le lettere. Lascia la punteggiatura e la "a" e la "I"
    tweet = re.sub("i'm", "I'm", tweet)
    tweet = re.sub("i'd", "I'd", tweet)
    tweet = re.sub("i'll", "I'll", tweet)
    tweet = re.sub("i've", "I have", tweet)
    wordlist = tweet.split()
    clean_text = ''
    words = []
    for w in wordlist:
        if (len(w) == 1): # se ha dimensione pari a 1 potrebbe anche essere un carattere di punteggiatura
            n = ord(w)
            if not ((64 < n < 91) or (96 < n < 123)): # se non è un carattere alfabetico, lo mantengo
                words.append(w)
            if (w == 'I'):
                words.append(w)
            if (w == 'i'):
                w = w.upper()
                words.append(w)
            if (w == 'a'):
                words.append(w)
        else:
            words.append(w)
        clean_text = ' '.join(words)

    clean_text = re.sub('^( )*\.', "", clean_text)  # elimino il punto quando è il primo carattere della stringa
    return clean_text