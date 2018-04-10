import pandas as pd
import csv
import numpy as np

data=pd.read_csv('../Data/ikt.csv')
x=data.news

newdata=[]

for i in x:
	
	newdata.append(i.replace("www.oxu.az"," "))

#newdata.to_csv('newdata.csv', index=False)

with open('newdata.csv', 'w',encoding="utf8") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(newdata)

