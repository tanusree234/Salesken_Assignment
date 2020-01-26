import pandas as pd
import nltk
import time
import csv
import os

#Creating row header for result
row_list = [["Correct_Name", "Misspelt_Name", "Id"]]

#Reading CSV
misspeltDf=pd.read_csv('C:\Anaconda2\Python Programs\Misspelt_cities.csv')
correctDf=pd.read_csv('C:\Anaconda2\Python Programs\Correct_cities.csv')

n=len(misspeltDf)

'''
Checking the time
'''
start_time = time.time()
for i in range(1,n):
    #List of Cities from the same country
    cts=(correctDf[correctDf['country'] == misspeltDf['country'].iloc[i]])
    #Initiating minimum distance and city name for storing temporarily
    minDis=99999999
    nm=''
    for ct in cts['name']:
        misCt=misspeltDf['misspelt_name'].iloc[i]
        
        #Checking the length of correct and misspelt city
        if len(misCt)==len(ct):
            dis=nltk.edit_distance(ct, misCt)
            if dis<minDis:
                minDis=dis
                nm=ct
    #Appending all ids in Row list
    row_list.append([nm, misCt,correctDf.loc[correctDf['name']==nm,'id'].tolist()[0]])
print("--- %s seconds ---" % (time.time() - start_time))

print(row_list)

with open('C:\Anaconda2\Python Programs\CityIdList.csv', 'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)   
    
print('done')