#! /Users/andrewbruckman/anaconda/bin/python

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:25:09 2017

@author: James
"""

import json
import numpy as np
from sklearn.base import TransformerMixin
import pickle
import sys
class EnsembleTranformer(TransformerMixin):
        def __init__(self, model, y):
            self.model = model
            self.y = y
        def transform(self,X,  **transform_params):
            return np.array([self.model.predict(X)]).T
 # pipeline = feature union of EnsembleTranformer
        def fit(self, X, y=None, **fit_params):
            self.model.fit(X, y)
            return self

def PostgressCall():
    conn = psycopg2.connect("host='localhost' port='5432' dbname='Ekodev' user='bn_openerp' password='fa05844d'")

def jsonInterp(JSONFile, Feature_Columns):

    cptCodes = []
    ResultsList = []
    with open(JSONFile) as data_file:
        data = json.load(data_file)
        for i  in data['cptstring'].split(","):
            cptCodes += [i.strip(" ").rstrip(" ")]
        Procedure= data['pocedure']
        Room = data['number_of_rooms']

        for num, i in enumerate(Feature_Columns):

            if i == '1r':
                pass

            elif i[0].isdigit():
                if i in cptCodes:
                    ResultsList += [1]
                else:
                    ResultsList += [0]
            else:
                if i == Procedure:
                    ResultsList += [1]

                else:
                    ResultsList += [0]

    return np.array(ResultsList)



def main(JSONFile):
    feature_cols =  ['63685', '63650', 'Radiofrequency', 'Lumbar Radiofrequency', '64635', '64636', 'ESI' ]

    JSONList = jsonInterp(JSONFile,feature_cols)
    #print JSONList
    algagain = pickle.load( open( "Alg_Improved_Whole_Year3.p", "rb" ) )
    if algagain.predict(np.array(JSONList)) > 200 or algagain.predict(np.array(JSONList)) < -200:
        print 34.0
        return 34.0
    else:
        print algagain.predict(np.array(JSONList))[0]
        return algagain.predict(np.array(JSONList))[0]


if __name__ == '__main__':
    JSONFile = sys.argv[1]
    main(JSONFile)
#JSONFile = 'temp.json'


#print main(JSONFile)



"""
feature_cols =['63685', '63650', 'Radiofrequency', 'Lumbar Radiofrequency', '64636', '64635', 'ESI', '1r']
WholeYearDF = pd.read_csv('WholeYear.csv')
OOSDF = WholeYearDF#[WholeYearDF['Date'] > '10/03/2016']

difflist = []
diffDict = {'pred':[], 'actual':[] , 'difference':[]}
for i in range(len(OOSDF)):
     OOSRow = list(OOSDF[feature_cols].iloc[i])
     print OOSRow
     print '555'
     pred = main(OOSRow)[0]
     actual = OOSDF['TotalTimeMin'].iloc[i]


     print pred, actual, pred-  actual
     difflist += [pred - actual]
     diffDict['pred'] += [pred]
     diffDict['actual'] += [actual]
     diffDict['difference'] += [pred - actual]
dictDF = pd.DataFrame.from_dict(diffDict)
dictDF.to_csv("PredVActual.csv")
diffarray = abs(np.array(difflist))
print diffarray.mean()
sqrtsquarederror = np.sqrt(np.square(-np.array(difflist)))

codelist =[]
for i in WholeYearDF['CPTCode']:
    print i
    if 'noCPT' not in i[0]:
        codelist += [i[0]]
"""
