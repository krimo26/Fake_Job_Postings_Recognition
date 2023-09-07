#Mirko Manset mat.309308

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder

#Importo il dataset di partenza
df=pd.read_csv("fake_job_postings.csv")

#Valuto in generale il dataset
df.info()
print()
print(df.head())
print()

#Conto gli elemnti mancanti ed elimino le features con troppi valori mancanti (in questo caso 'department' e 'salary_range')
print("Counting missing values")
print(df.isnull().sum())
df = df.drop(['department', 'salary_range'], axis=1)

print()
print("Removing 'department' and 'salary_range")
df.info()
print()
print(df.head())
print()

#Esploro il dataset: le variabili sono categoriche? Se le opzioni sono poche ne valuto la distribuzione altrimenti si tratta di una variabile non strutturata (testuale)
#Le caso in cui le opzioni sono solo 2 allora si tratta di variabili binarie
#In questo caso riconosco come variabili categoriche 'employment_type', 'required_experience', 'required_education', 'function'
#Riconosco invece come variabili binare: 'fraudulent' (anche il target), 'telecommuting', 'has_company_logo', 'has_questions'

print("Counting unique values")
print(df.nunique())
print()
print()

feat = list()

fraudulent = (df["fraudulent"].value_counts(), "fraudulent")

telecom = (df["telecommuting"].value_counts(),"telecommuting")
logo = (df["has_company_logo"].value_counts(),"has_company_logo")
questions = (df["has_questions"].value_counts(),"has_questions")

employment = (df["employment_type"].value_counts(),"employment_type")
experience = (df["required_experience"].value_counts(), "required_experience")
education = (df["required_education"].value_counts(), "required_education")
function = (df["function"].value_counts(), "function")

feat.append(fraudulent)

feat.append(telecom)
feat.append(logo)
feat.append(questions)

feat.append(employment)
feat.append(experience)
feat.append(education)
feat.append(function)

#Plot delle distribuzioni

for data in feat:
	print("Distribution of ", data[1])
	print(data[0])
	print()
	ax = sns.countplot(x=data[1], data=df)
	if (data[1] == 'function' or data[1] == 'required_education'):
		plt.xticks(fontsize = 5, rotation='vertical')
	plt.show()
	

	
	
#Per le altre features testuali  creo un'unica stringa di testo che aggiungo come feature 'text'
#Prima di tutto sostituisco i valori null con uno spazio
#Successivamente costruisco la feature 'text' concatenando le altre features (considero anche la feature 'function' per evitare troppe features nella successiva codifica one-hot)
#Infine scrivo il nuovo dataset csv


df["location"].fillna(" ", inplace = True)
df["company_profile"].fillna(" ", inplace = True)
df["description"].fillna(" ", inplace = True)
df["requirements"].fillna(" ", inplace = True)
df["benefits"].fillna(" ", inplace = True)
df["industry"].fillna(" ", inplace = True)
df["function"].fillna(" ", inplace = True)

df['text'] = df['title']+" "+df['location']+" "+df['company_profile']+" "+df['description']+" "+df['requirements']+" "+df['benefits']+" " +df['industry']+" "+df['function']
df = df.drop(['job_id', 'title', 'location', 'company_profile', 'description', 'requirements', 'benefits', 'industry', 'function'], axis=1)

#df.to_csv("unified.csv",index=False)

#Una volta formato il nuovo dataset costruisco quello pulito utilizzando il codice di cleaning opportunamente modificato
#Il risultato finale è il dataset con la feature 'text' pulita 

print()
print()
print("Now using clean dataset")
print()
clean=pd.read_csv("corpus_clean.csv")
clean.info()
print()
print(clean.head())

#Infine codifico le variabili categoriche con la codifica one-hot
#Scrivo il dataset finale in csv

clean = pd.get_dummies(clean, columns=["employment_type"])
clean = pd.get_dummies(clean, columns=["required_experience"])
clean = pd.get_dummies(clean, columns=["required_education"])

#clean.to_csv("final_dataset.csv",index=False)

print()
print()
print("Now using final dataset")
print()
final=pd.read_csv("final_dataset.csv")
final.info()
print()
print(final.head())


