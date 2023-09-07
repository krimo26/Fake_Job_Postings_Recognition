# -*- coding: utf-8 -*-
import re
from nltk.tokenize import TweetTokenizer
import string
import nltk

def cleaner(tweet):
    """convert the insults in badWord"""
    text = tweet

    # ricerca di insulti e parolacce:
    text = re.sub((' fuck you '), " badWord ", text)
    text = re.sub((' fuck off '), " badWord ", text)
    text = re.sub((' faggot '), " badWord ", text)
    text = re.sub((' son of a bitch '), " badWord ", text)
    text = re.sub((' bastard '), " badWord ", text)
    text = re.sub((' asshole '), " badWord ", text)
    text = re.sub((' scumbag '), " badWord ", text)
    text = re.sub((' whore '), " badWord ", text)
    text = re.sub((' idiot '), " badWord ", text)
    text = re.sub((' dickhead '), " badWord ", text)
    text = re.sub((' dumbass '), " badWord ", text)
    text = re.sub((' fatass '), " badWord ", text)
    text = re.sub((' motherfucker '), " badWord ", text)
    text = re.sub((' pussy '), " badWord ", text)
    text = re.sub((' sucker '), " badWord ", text)
    text = re.sub((' twat '), " badWord ", text)
    text = re.sub((' dick '), " badWord ", text)
    text = re.sub((' shit '), " badWord ", text)
    text = re.sub((' bitch '), " badWord ", text)
    text = re.sub((' ass '), " badWord ", text)
    text = re.sub((' Fuck you '), " badWord ", text)
    text = re.sub((' Fuck off '), " badWord ", text)
    text = re.sub((' Faggot '), " badWord ", text)
    text = re.sub((' Son of a bitch '), " badWord ", text)
    text = re.sub((' Bastard '), " badWord ", text)
    text = re.sub((' Asshole '), " badWord ", text)
    text = re.sub((' Scumbag '), " badWord ", text)
    text = re.sub((' Whore '), " badWord ", text)
    text = re.sub((' Idiot '), " badWord ", text)
    text = re.sub((' Dickhead '), " badWord ", text)
    text = re.sub((' Dumbass '), " badWord ", text)
    text = re.sub((' Fatass '), " badWord ", text)
    text = re.sub((' Motherfucker '), " badWord ", text)
    text = re.sub((' Pussy '), " badWord ", text)
    text = re.sub((' Sucker '), " badWord ", text)
    text = re.sub((' Twat '), " badWord ", text)
    text = re.sub((' Dick '), " badWord ", text)
    text = re.sub((' Shit '), " badWord ", text)
    text = re.sub((' Bitch '), " badWord ", text)
    text = re.sub((' Ass '), " badWord ", text)

    # ricerca di parole censurate da asterischi o altri simboli:
    text = re.sub(('f\*\*k'), " badWord ", text)
    text = re.sub(('d\*\*k'), " badWord ", text)
    text = re.sub(('s\*\*t'), " badWord ", text)
    text = re.sub(('sh\*\*'), " badWord ", text)
    text = re.sub(('sh\*\*less'), " badWord ", text)
    text = re.sub(('f\*\*kin'), " badWord ", text)
    text = re.sub(('b\*\*ches'), " badWord ", text)
    text = re.sub(('b\*\*ch'), " badWord ", text)
    text = re.sub(('n\*\*ga'), " badWord ", text)
    text = re.sub(('a\*\*'), " badWord ", text)
    text = re.sub(('f##k'), " badWord ", text)
    text = re.sub(('f##kin'), " badWord ", text)
    text = re.sub(('f\-\-k'), " badWord ", text)

    return text
