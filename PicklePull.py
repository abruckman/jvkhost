
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:25:09 2017

@author: James
"""

import json
import numpy as np
from sklearn.base import TransformerMixin
from sklearn import linear_model
import pickle
import sys
class EnsembleTranformer(TransformerMixin):
        def __init__(self, model, y):
            self.model = model
            self.y = y
        def transform(self,X,  **transform_params):
            return np.array([self.model.predict(X)]).T

        def fit(self, X, y=None, **fit_params):
            self.model.fit(X, y)
            return self
            
    
def jsonInterp(JSONFile, Feature_Columns):
    
    cptCodes = []
    ResultsList = []
    with open(JSONFile) as data_file:    
        data = json.load(data_file)
        for i  in data['cptstring'].split(","):
            cptCodes += [i.strip(" ").rstrip(" ")]
        Procedure= data['procedure']
        Room = data['number_of_rooms']
        
        for num, i in enumerate(Feature_Columns):
            
            if i == '1r':
                if Room == "One Room":
                    ResultsList += [0]
                elif Room == "Unknown":
                    ResultsList += [1]
                else:
                    ResultsList += [1]
                    
            elif i[0].isdigit():
                if i in cptCodes:
                    ResultsList += [1]
                else:
                    ResultsList += [0]
            else:
                #print Procedure
                if i == 'ESI' and 'ESI' in Procedure:
                    ResultsList += [1]
                elif i== 'Radiofrequency' and 'Radiofrequency' in Procedure:
                    ResultsList += [1]
                elif i== 'Lumbar Radiofrequency' and 'Lumbar Radiofrequency' in Procedure:
                    ResultsList += [1]
                    
                else:
                    ResultsList += [0]
                    
    return np.array(ResultsList)   
                    
                
                
def main(JSONFile):
    feature_cols =  ['63685', '63650', 'Radiofrequency', 'Lumbar Radiofrequency', '64635', '64636', 'ESI','1r' ]     
      
    JSONList = jsonInterp(JSONFile,feature_cols)
    
    algagain = pickle.load(open("Alg_Huber_Whole_Year_Room.p", "rb" ) )
    if algagain.predict(np.array(JSONList)) > 200 or algagain.predict(np.array(JSONList)) < -200:
        if '63865' in str(JSONList) and '63650'  in str(JSONList):
            
            print 113
            return 113
        elif '63650' in str(JSONList) or '63865' in str(JSONList):
            print "60 Minutes 23 Seconds"
            return 60.2
        else:
            print "28 Minutes 2 Seconds"
            return 28
    else:
        value = algagain.predict(np.array(JSONList))[0]
        print str(int(value)) + " Minutes " + str(int(float("." + str(value-int(value)).split('.')[1]) * 60)) + " Seconds"
        return value
        

if __name__ == '__main__':
    JSONFile = sys.argv[1]
    main(JSONFile) 


#JSON = "temp.json"
#main(JSON)


