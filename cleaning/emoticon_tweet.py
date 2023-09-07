# -*- coding: utf-8 -*-
import re


def cleaner(tweet):
    """convert the emoticons in the sentiment group"""
    clean_text = tweet

    # Il preprocessing è leggermente differente da quello delle recensioni, poichè sono stati rimossi gli spazi
    # Nei social è uso comune scrivere le emoticon senza spazi

    # From Wikipedia
    # angel, innocent
    clean_text = re.sub(r"O:\-\)|0:\-3|0:3|0:\-\)|0:\)|0;\^\)|\(\-:O|\(\-:0|\(:O|\(:0|\(\^:0|\(\^:O", " smileAngel ", clean_text)
    # evil
    clean_text = re.sub(r">:\)|>;\)|>:\-\)|\}:\-\)|}:\)|3:\-\)|3:\)|\(:<|\(;<|\(\-:<|\(\-;<|\(\-:\{|\(:\{", " smileEvil ", clean_text)
    # happy
    clean_text = re.sub(r":\-\)|:\)|:D|:o\)|:O\)|:\]|:3|:c\)|:>|=\]|8\)|=\)|:\}|:\^\)|\^_\^|=:\)|\(:|\(\-:|\(o:|\(O:|\[:|<:|\[=|\(8|\(=|\{:|\(\^:", " smileHappy ", clean_text)
    # laugh
    clean_text = re.sub(r":\-D|8\-D|8D|x\-D|xD|X\-D|XD|=\-D|=D|=\-3|=3|B\^D|:\-\)\)|:'\-\)|:'\)", " smileLaugh ",
                        clean_text)
    # angry
    clean_text = re.sub(r":\-\|\||:@|>:\(|\|\|\-:|@:|\):<", " smileAngry ", clean_text)
    # sad
    clean_text = re.sub(r">:\[|:\-\(|:\(|:\-c|:c|:\-<|:\-\[|:\[|:\{|<\\3|\]:<|\)\-:|\):|>\-:|\]\-:|\]:|\}:", " smileSad ", clean_text)
    # crying
    clean_text = re.sub(r";\(|:'\-\(|:'\(|\);|\)':|\)\-':", " smileCrying ", clean_text)
    # horror, disgust
    clean_text = re.sub(r"D:<|D:|D8|D;|D=|DX|v\.v|D\-':", " smileFear ", clean_text)
    # surprise, shock
    clean_text = re.sub(r">:O|:\-O|:O|:\-o|:o|8\-0|O_O|o\-o|O_o|o_O|o_o|O\-O|#_#|O:<|O\-:|O:|o\-:|o:|0\-8", " smileSurprise ", clean_text)
    # kiss
    clean_text = re.sub(r":\*|:\-\*|:\^\*|\( '\}\{' \)|<3|\*:|\*\-:|\*\^:", " smileKiss ", clean_text)
    # winking
    clean_text = re.sub(r";\-\)|;\)|\*\-\)|\*\)|;\-\]|;\]|;D|;\^\)|:\-,|\(;|\(\-;|\[;|\[\-;|\(\^;", " smileWink ", clean_text)
    # tongue sticking out
    clean_text = re.sub(r">:P|:\-P|:P|X\-P|x\-p|xp|XP|:\-p|:p|=p|:\-Þ|:Þ|:þ|:\-þ|:\-b|:b|d:",
                        " smileTongueStickingOut ", clean_text)
    # skeptical
    clean_text = re.sub(r">:\\|>:/|:\-/|:\-\.|:/|:\\|=/|=\\|:L|=L|:S|:s|>\.<|\-_\-|/:<|\\:<|\\\-:|/\-:|\.\-:|/:|\\:|/=|\\=|S:|s:", " smileSkeptical ", clean_text)
    # straight face
    clean_text = re.sub(r":\||:\-\||\|:|\|\-:", " smileStraightFace ", clean_text)

    # after the emoticons, remove the hashtag:
    clean_text = re.sub(r"#\S+", " ", clean_text)

    # remove not ASCII chars and numbers
    tmp = ''
    for c in clean_text:
        if (ord(c) < 128):
            tmp += c
    clean_text = tmp

    return clean_text