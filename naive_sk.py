from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pandas as pd 
import numpy as np
from sklearn.utils import shuffle
from sklearn.externals import joblib
from sklearn.svm import SVC
import csv 
import string

data_old=pd.read_csv('../Data/combine.csv')
#data_old.replace(r)
shuffled = shuffle(data_old)
shuffled.to_csv('newfile.csv', index=False)

data=pd.read_csv('newfile.csv')


train_data = data[:int((len(data)+1)*.80)] #Remaining 80% to training set
test_data = data[int(len(data)*.80+1):] #Splits 20% data to test se






x=train_data.news
y=train_data.label

vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(x.values.astype('U'))

#print(vectorizer.vocabulary_)


#print(X_train_counts.shape)





tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape


tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

#text_clf = SVC(probability=True)
																												
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
])

text_clf.fit(x.values.astype('U'), y.values.astype('U'))

docs_test=test_data.news.values.astype('U')
predicted = text_clf.predict(docs_test)
#predicted_probab=text_clf.predict_proba(docs_test)
print (predicted)
#print(predicted_probab)



print(np.mean(predicted == test_data.label.astype('U')) )    


#joblib.dump(text_clf, 'svm.pkl')       

