from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import pandas as pd 
import numpy as np
from random import shuffle


data=pd.read_csv('../Data/all_data.csv')
#x=data.news
#y=data.label

vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(data.news.values.astype('U'))
#print(vectorizer.vocabulary_)


'''
X_train_counts.shape

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape


tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

																												
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, 
                                           max_iter=5, tol=None)),
])
text_clf.fit(x, y)



#test =pd.read_csv('../Data/test.csv')
#docs_test=test.news


#predicted = text_clf.predict(docs_test)
#print(predicted)


#print(np.mean(predicted == test.label) )           

'''