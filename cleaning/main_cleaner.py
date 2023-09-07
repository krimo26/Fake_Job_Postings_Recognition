# coding=utf-8
import nltk
import string
import negation
import punctuation_multi
import spaces
import lower
import string
import nltk.tag
import insult
import emoticon_tweet
import slang
import symbol_punct
import url
import single_chars
import forme_contratte
import re
import pprint
import stopwords
import stemming
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')

# Apro il file con le frasi da pulire 
file_in = pd.read_csv("unified.csv",sep=",") 

# Apro il file di output per la scrittura
file_out = open("corpus_clean.csv","w+")
file_out.write("telecommuting,has_company_logo,has_questions,employment_type,required_experience,required_education,fraudulent,text\n")


for index,row in file_in.iterrows():
  
	telecom = row["telecommuting"]
	logo = row["has_company_logo"]
	questions = row["has_questions"]
	employment = row["employment_type"]
	experience = row["required_experience"]
	education = row["required_education"]
	fraud = row["fraudulent"]

	sentence = row["text"]

	clean_text = url.cleaner(sentence)
	clean_text = emoticon_tweet.cleaner(clean_text)
	clean_text = insult.cleaner(clean_text)
	clean_text = slang.cleaner(clean_text)
	clean_text = symbol_punct.cleaner(clean_text)
	clean_text = spaces.cleaner(clean_text)
	clean_text = lower.cleaner(clean_text)
	clean_text = negation.cleaner(clean_text)
	clean_text = stopwords.cleaner(clean_text)
	clean_text = stemming.cleaner(clean_text)
	clean_text = forme_contratte.cleaner(clean_text)
	clean_text = punctuation_multi.cleaner(clean_text)
	clean_text = single_chars.cleaner(clean_text)
	clean_text = spaces.cleaner(clean_text)

	# Ricostruisco l'istanza con la frase e la sua classe
	new_line =  str(telecom)+","+str(logo)+","+str(questions)+","+str(employment)+","+str(experience)+","+str(education)+","+str(fraud)+","+'"'+clean_text+'"'+"\n"
	file_out.write(new_line)

file_out.close()
