#Mirko Manset mat.309308

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,precision_score,recall_score,f1_score
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

#Leggo il dataset costruito in preprocessing
df=pd.read_csv("final_dataset.csv")

#Individuo il target: 'fraudulent'
y = df.pop('fraudulent')
X = df

#Imparo il vocabolario dalla feature 'text' e ricostruisco il nuovo datagram aggingendo le features del dizionario
vectorizer = TfidfVectorizer(max_features = 10000,ngram_range=(1,3))
vectorizer.fit(X['text'])

dictionary = vectorizer.get_feature_names()
bow_features = vectorizer.transform(X.pop('text')).toarray()

bow_df = pd.DataFrame(bow_features,columns=dictionary)
X = pd.concat([X,bow_df],axis=1)
X.info()
print(X.head())
print()

#Divido training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, stratify=y)

#K fold: 5 fold per valutare ogni modello 5 volte per poi trarne le performance sulla media (anche in fase di fine tuning)
print("Let's use k fold for some models")
n_fold=5

logsumprecision = 0
logsumrecall = 0
logsumscore = 0

rforsumprecision = 0
rforsumrecall = 0
rforsumscore = 0

adasumprecision = 0
adasumrecall = 0
adasumscore = 0

gradsumprecision = 0
gradsumrecall = 0
gradsumscore = 0

i = 1

kf =KFold(n_splits=n_fold, random_state=None, shuffle=False) 

for train_index, validation_index in kf.split(X):
	X_train = X[train_index[0]:train_index[-1]]
	X_validation = X[validation_index[0]:validation_index[-1]]
	y_train= y[train_index[0]:train_index[-1]]
	y_validation = y[validation_index[0]:validation_index[-1]]

	#Logistic regression
	logreg = LogisticRegression(solver="liblinear")
	logreg.fit(X_train, y_train)
	y_pred = logreg.predict(X_validation)
	
	logsumprecision += precision_score(y_validation,y_pred)
	logsumrecall += recall_score(y_validation,y_pred)
	logsumscore += f1_score(y_validation,y_pred)
	print("Logistic Regression ", i)
	
	#RandomForest	
	rforest= RandomForestClassifier(n_estimators = 100)
	rforest.fit(X_train,y_train)
	y_pred = rforest.predict(X_validation)
	
	rforsumprecision += precision_score(y_validation,y_pred)
	rforsumrecall += recall_score(y_validation,y_pred)
	rforsumscore += f1_score(y_validation,y_pred)
	print("Random Forest ", i)
	
	#AdaBoost	
	ada= AdaBoostClassifier(n_estimators = 100)
	ada.fit(X_train,y_train)
	y_pred = ada.predict(X_validation)
	
	adasumprecision += precision_score(y_validation,y_pred)
	adasumrecall += recall_score(y_validation,y_pred)
	adasumscore += f1_score(y_validation,y_pred)
	print("AdaBoost ", i)
	
	#GradientBoost
	grad= GradientBoostingClassifier(n_estimators = 100)
	grad.fit(X_train,y_train)
	y_pred = grad.predict(X_validation)
	
	gradsumprecision += precision_score(y_validation,y_pred)
	gradsumrecall += recall_score(y_validation,y_pred)
	gradsumscore += f1_score(y_validation,y_pred)
	print("GradientBoost ", i)
	
	
	print()
	i += 1
	
print('Logistic Regression - Average precision: ', logsumprecision/n_fold)
print('Logistic Regression - Average recall: ', logsumrecall/n_fold)	
print('Logistic Regression - Average f1_score: ', logsumscore/n_fold)	
print()

print('Random Forest - Average precision: ', rforsumprecision/n_fold)
print('Random Forest - Average recall: ', rforsumrecall/n_fold)	
print('Random Forest - Average f1_score: ', rforsumscore/n_fold)
print()	

print('AdaBoost - Average precision: ', adasumprecision/n_fold)
print('AdaBoost - Average recall: ', adasumrecall/n_fold)	
print('AdaBoost - Average f1_score: ', adasumscore/n_fold)
print()	

print('GradientBoost - Average precision: ', gradsumprecision/n_fold)
print('GradientBoost - Average recall: ', gradsumrecall/n_fold)	
print('GradientBoost - Average f1_score: ', gradsumscore/n_fold)	
print()


#Uso Random Forest: fine tuning - scelta di max_depth (valuto ancora la performance in media con k-fold)

print()
print("Using RandomForest")
print()
print("Let's fine tune max_depth")
print()
max_depth_array = [10,100,1000,10000]

trainarray = [0]*4
testarray = [0]*4
i = 0

kf =KFold(n_splits=n_fold, random_state=None, shuffle=False) #initialize KFold

for val in max_depth_array:

	sum_prec_test = 0
	sum_rec_test = 0
	sum_score_test = 0
	
	sum_prec_train = 0
	sum_rec_train = 0
	sum_score_train = 0
	
	j=1
	
	print("max_depth = ",val)
	for train_index, validation_index in kf.split(X):
		X_train = X[train_index[0]:train_index[-1]]
		X_validation = X[validation_index[0]:validation_index[-1]]
		y_train= y[train_index[0]:train_index[-1]]
		y_validation = y[validation_index[0]:validation_index[-1]]
		
		rf_regr= RandomForestClassifier(n_estimators = 100, max_depth = val)
		rf_regr.fit(X_train,y_train)
		
		y_pred = rf_regr.predict(X_validation)
		y_predtrain = rf_regr.predict(X_train)
		
		sum_prec_test += precision_score(y_validation,y_pred)
		sum_rec_test += recall_score(y_validation,y_pred)
		sum_score_test += f1_score(y_validation,y_pred)
		
		sum_prec_train += precision_score(y_train,y_predtrain)
		sum_rec_train += recall_score(y_train,y_predtrain)
		sum_score_train += f1_score(y_train,y_predtrain)
		
		
	print('Test: Avarage f1_score: ', sum_score_test/n_fold)
	testarray[i] = sum_score_test/n_fold
	
	print('Train: Avarage f1_score: ', sum_score_train/n_fold)
	trainarray[i] = sum_score_train/n_fold
	print()
	i = i+1

#Plot delle performance in train e validation		
plt.plot([0,1,2,3],trainarray,"r-",label="Train F1_score")
plt.plot([0,1,2,3],testarray,"b-",label="Test F1_score")
plt.xlabel("")
plt.ylabel("F1_Score")
plt.legend()
plt.show()


#Fine tuning - scelta di min_samples_split (valuto ancora la performance in media con k-fold)

print()
print("Let's fine tune min_samples_split")
print()
print()
min_samples_split_array = [2,5,10,40]

trainarray = [0]*4
testarray = [0]*4
i = 0

kf =KFold(n_splits=n_fold, random_state=None, shuffle=False) #initialize KFold

for val in min_samples_split_array:

	sum_prec_test = 0
	sum_rec_test = 0
	sum_score_test = 0
	
	sum_prec_train = 0
	sum_rec_train = 0
	sum_score_train = 0
	
	j=1
	
	print("min_samples_split = ",val)
	for train_index, validation_index in kf.split(X):
		X_train = X[train_index[0]:train_index[-1]]
		X_validation = X[validation_index[0]:validation_index[-1]]
		y_train= y[train_index[0]:train_index[-1]]
		y_validation = y[validation_index[0]:validation_index[-1]]
		
		rf_regr= RandomForestClassifier(n_estimators = 100, max_depth= 100, min_samples_split = val)
		rf_regr.fit(X_train,y_train)
		
		y_pred = rf_regr.predict(X_validation)
		y_predtrain = rf_regr.predict(X_train)
		
		sum_prec_test += precision_score(y_validation,y_pred)
		sum_rec_test += recall_score(y_validation,y_pred)
		sum_score_test += f1_score(y_validation,y_pred)
		
		sum_prec_train += precision_score(y_train,y_predtrain)
		sum_rec_train += recall_score(y_train,y_predtrain)
		sum_score_train += f1_score(y_train,y_predtrain)
		
		
		
	print('Test: Avarage f1_score: ', sum_score_test/n_fold)
	testarray[i] = sum_score_test/n_fold
	
	print('Train: Avarage f1_score: ', sum_score_train/n_fold)
	trainarray[i] = sum_score_train/n_fold
	print()
	i = i+1
	
#Plot delle performance in train e validation			
plt.plot([0,1,2,3],trainarray,"r-",label="Train f1_score")
plt.plot([0,1,2,3],testarray,"b-",label="Test fi_score")
plt.xlabel("")
plt.ylabel("F1_Score")
plt.legend()
plt.show()



#Uso Random Forest con max_depth = 100 e min_samples_split = 2
print("Using RandomForest max_depth = 100 e min_samples_split = 2")
print()

rforest= RandomForestClassifier(n_estimators = 100, max_depth=100, min_samples_split=2)
rforest.fit(X_train,y_train)

y_pred = rforest.predict(X_test)
print("Confiusion matrix:")
print(confusion_matrix(y_test,y_pred))

print("Precision: ", precision_score(y_test,y_pred))

print("Recall: ", recall_score(y_test,y_pred))

print("F1 score: ", f1_score(y_test,y_pred))
print()


