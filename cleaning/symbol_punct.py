# -*- coding: utf-8 -*-
import re


def cleaner(tweet):
    """remove punctuation repeated and other symbols"""
    clean_text = tweet

    # I titoli personali vanno convertiti con la maiuscola e senza il punto
    # Mr
    clean_text = re.sub(r' Mr\.', ' Mr ', clean_text)   # Mr.Black oppure Mr. Black
    clean_text = re.sub(r'^Mr\.', 'Mr ', clean_text)    # Come sopra, a inizio frase
    clean_text = re.sub(r' mr\.', ' Mr ', clean_text)   # mr.Black oppure mr. Black
    clean_text = re.sub(r'^mr\.', 'Mr ', clean_text)    # Come sopra, a inizio frase
    clean_text = re.sub(r' mr ', ' Mr ', clean_text)    # mr Black
    clean_text = re.sub(r'^mr ', 'Mr ', clean_text)    # mr Black a inizio frase
    # Mrs
    clean_text = re.sub(r' Mrs\.', ' Mrs ', clean_text) # Mrs.Black oppure Mrs. Black
    clean_text = re.sub(r'^Mrs\.', 'Mrs ', clean_text)  # Come sopra, a inizio frase
    clean_text = re.sub(r' mrs\.', ' Mrs ', clean_text) # mrs.Black oppure mrs. Black
    clean_text = re.sub(r'^mrs\.', 'Mrs ', clean_text)  # Come sopra, a inizio frase
    clean_text = re.sub(r' mrs ', ' Mrs ', clean_text)  # mrs Black
    clean_text = re.sub(r'^mrs ', 'Mrs ', clean_text)  # mrs Black a inizio frase
    # Dr
    clean_text = re.sub(r' Dr\.', ' Dr ', clean_text)   # Dr.Black oppure Dr. Black
    clean_text = re.sub(r'^Dr\.', 'Dr ', clean_text)    # Come sopra, a inizio frase
    clean_text = re.sub(r' dr\.', ' Dr ', clean_text)   # dr.Black oppure dr. Black
    clean_text = re.sub(r'^dr\.', 'Dr ', clean_text)    # Come sopra, a inizio frase
    clean_text = re.sub(r' dr ', ' Dr ', clean_text)    # dr Black
    clean_text = re.sub(r'^dr ', 'Dr ', clean_text)     # dr Black a inizio frase

    # Acronimi noti
    clean_text = re.sub(r' U\.S\. ', ' United States ', clean_text)
    clean_text = re.sub(r' US ', ' United States ', clean_text)
    clean_text = re.sub(r' U\.S\.A\. ', ' United States ', clean_text)
    clean_text = re.sub(r' USA ', ' United States ', clean_text)
    clean_text = re.sub(r'o\.k\.', ' ok ', clean_text)
    clean_text = re.sub(r'o\.k', ' ok ', clean_text)
    clean_text = re.sub(r'O\.K\.', ' ok ', clean_text)
    clean_text = re.sub(r'O\.K', ' ok ', clean_text)
    clean_text = re.sub(r'O\.k\.', ' ok ', clean_text)
    clean_text = re.sub(r'O\.k', ' ok ', clean_text)

    # clean the h in the laugh
    clean_text = re.sub('hh+', "h", clean_text)
    clean_text = re.sub('aaa+', "a", clean_text)
    clean_text = re.sub(r'(ah){2,}|(ha){2,}', " laughtTag ", clean_text)

    # remove the symbols and parentheses
    clean_text = re.sub(r'(\(|\)|\-|\[|\]|\{|\}|\*|\||\<|\>|%|/|$|\+|@|#|\$|£|=|\^|~|€|_|")', " ",
                        clean_text)

    # come sotto, ma a inizio frase
    clean_text = re.sub(r'^(\. ){2,}(\.( )*)*', ' multiPoint ', clean_text)
    clean_text = re.sub(r'^\.\.+', ' multiPoint ', clean_text)
    clean_text = re.sub(r'^,,+', ' multiPoint ', clean_text)

    # salvo la sequenza di punti con un tag specifico
    clean_text = re.sub(r'(\. ){2,}(\.( )*)*', ' multiPoint ', clean_text)      # tre puntini di sospensione staccati
    clean_text = re.sub(r'\.\.+', ' multiPoint ', clean_text)                   # tre puntini di sospensione uniti
    clean_text = re.sub(r',,+', ' multiPoint ',clean_text)                      # tre puntini di sospensione con le virgole


    # E' importante cercare prima i 3 puntini staccati e poi quelli uniti, altrimenti una sequenza come questa:
    #  . . ... . .
    # non verrebbe riconosciuta, estrapolando solo i 3 puntini centrali ed escludendo quelli ai lati

    # NOMI PROPRI con iniziali
    clean_text = re.sub(r' ([A-Z]\.)+(?P<second>[A-Z][a-z])', r'\g<second>',clean_text)  # Conservo il nome eliminando l'iniziale e il punto
    clean_text = re.sub(r'([A-Z]\.)+(?P<second>[A-Z][a-z])', r'\g<second>', clean_text)  # Come sopra ma a inizio frase

    # ACRONIMI completi e incompleti
    clean_text = re.sub(r' ([A-Z]\.)+([A-Z](\.)*)+', ' ', clean_text)  # Elimina gli acronimi con o senza punto finale
    clean_text = re.sub(r'([A-Z]\.)+([A-Z](\.)*)+', ' ', clean_text)  # Come sopra, ma a inizio frase

    # gli unici punti rimasti sono solo quelli singoli: li separo solo se non sono in mezzo ai numeri
    clean_text = re.sub(r'(?P<first>\D)(\.)(?P<second>\D)', r'\g<first> . \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>\D)(\.)(?P<second>\D)', r'\g<first> . \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>\D)(\.)(?P<second>\d)', r'\g<first> . \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>\d)(\.)(?P<second>\D)', r'\g<first> . \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>.)(\.)$', r'\g<first> .', clean_text)
    clean_text = re.sub('^( )*\.', " ", clean_text)     # elimino il punto quando è il primo carattere della stringa

    # separo anche le virgole, per evitare problemi con le lettere singole
    clean_text = re.sub(r'(?P<first>\D)(,)(?P<second>\D)', r'\g<first> , \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>\D)(,)(?P<second>\D)', r'\g<first> , \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>\D)(,)(?P<second>\d)', r'\g<first> , \g<second>', clean_text)
    clean_text = re.sub(r'(?P<first>\d)(,)(?P<second>\D)', r'\g<first> , \g<second>', clean_text)

    # ULTIMA COSA DA FARE:
    # ripristino la sequenza di punti cercando il tag corrispondente
    clean_text = re.sub(r'^( )*multiPoint', " ", clean_text)   # se sono a inizio frase li elimino
    clean_text = re.sub(r'^( )*multiPoint', " ", clean_text)  # ripeto nel caso ci fossero 2 sequenze multiPoint
    clean_text = re.sub(r'multiPoint', " ... ", clean_text)


    # rimuovo le vocali ripetute per più di 3 volte
    clean_text = re.sub('[a]{3,}', "a", clean_text)
    clean_text = re.sub('[e]{3,}', "e", clean_text)
    clean_text = re.sub('[i]{3,}', "i", clean_text)
    clean_text = re.sub('[o]{3,}', "o", clean_text)
    clean_text = re.sub('[u]{3,}', "u", clean_text)

    return clean_text
