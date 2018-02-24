
import csv
import nltk

import tkinter as tk
from tkinter import *

from tkinter import font
from tkinter import messagebox
import pickle 


def processSentence(sentenece):
    sentenece = sentenece.lower()
    sentenece = sentenece.replace(',', '')
    sentenece = sentenece.replace('.', '')
  

    return sentenece

def getFeatureVector(sentenece):
	
	featureVector=[]
	words=sentenece.split(" ")
	
	
	for w in words:
	
		featureVector.append(w.lower())
	return featureVector

def extract_features(sentenece):
    sentenece_words = set(sentenece)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in sentenece_words)
    return features

def featurelistAndArray():
    featureList=[]
    inputsenteneces=csv.reader(open('Data/train.csv','r',encoding="utf8"))


    senteneces=[]
    for row in inputsenteneces:
	    sentenece=row[0]
	    sentiment=row[1]
	
	
	    processedsentenece=processSentence(sentenece)
	 
	    featureVector=getFeatureVector(processedsentenece)
	    featureList.extend(featureVector)

	    senteneces.append((featureVector,sentiment))


    featureList=list(set(featureList))
    return (featureList,senteneces)
featureList=featurelistAndArray()[0]
senteneces=featurelistAndArray()[1]


def show():
    top = Tk()
    RTitle=top.title("News Classfier")
    RWidth=top.winfo_screenwidth()
    RHeight=top.winfo_screenheight()
    top.geometry("%dx%d+0+0" % (RWidth, RHeight))


    
    S = Scrollbar(top)
    T = Text(top, x=RWidth/2-300, y=RHeight-600,width=600,height=300,bd=5)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    L1 = Label(top, text="Enter the text",font=("Helvetica", 20))
    L1.place(x=RWidth/2-100, y=100)





    #E1 = Entry(top, bd =5)
    #E1.place(x=RWidth/2-300, y=RHeight-600,width=600,height=300)
    #E1.icursor(-10)
    def get():
    	testsentenece=T.get("1.0","end-1c")
    	processed=processSentence(testsentenece)
    	classifier_f=open("naive.pickle","rb")
    	NBClassifier=pickle.load(classifier_f)
    	classifier_f.close()
    	result=NBClassifier.classify(extract_features(getFeatureVector(processed)))
    	

    	result_font=font.Font(family='Helvetica',size=18)
    	
    	L3=Label(top,text=result,fg='green',font=result_font)  
    	L3.place(x=RWidth/2-50, y=RHeight-190)
    	L2=Label(top,text="Type of the news is : ",font=result_font)
    	L2.place(x=RWidth/2-300, y=RHeight-190)
    	
    	

    button_font=font.Font(family='Helvetica',size=25)



    B1=Button(top,text="Check",command=get,bg='green',fg='white',font=button_font,activeforeground='green')
    B1.place(x=RWidth/2-120, y=RHeight-250,width=150,height=50)




  
    top.mainloop() 



'''def accuracychecker():
	counter=0
	inputTest=csv.reader(open('Data/test.csv','r'))
	for row in inputTest:
		sentenece=row[0]
		sentiment=row[1]
		testsentenece=sentenece
		processed=processSentence(testsentenece)
		training_set=nltk.classify.util.apply_features(extract_features,senteneces)
		NBClassifier=nltk.NaiveBayesClassifier.train(training_set)
		result=NBClassifier.classify(extract_features(getFeatureVector(processed)))
		if result==sentiment:
			counter+=1
		else:
			counter=counter
	print(counter)
'''

#main
show()




'''training_set=nltk.classify.util.apply_features(extract_features,senteneces)

NBClassifier=nltk.NaiveBayesClassifier.train(training_set)

save_classifier=open("naive.pickle","wb")
pickle.dump(NBClassifier,save_classifier)
save_classifier.close()'''


