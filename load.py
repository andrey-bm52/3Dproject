##!/usr/local/bin/python
## -*- coding: utf-8 -*-
import os
import json
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="andrey",
    passwd="andrey52",
    database="mydatabase1"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE dct (word VARCHAR(255), wordset_id VARCHAR(10), id VARCHAR(10), defn VARCHAR(255), example VARCHAR(255), speech_part VARCHAR(255), synonyms VARCHAR(255))")

# the result is a Python dictionary:
print('start')

# C:\\Users\\andrey.melnik\\Downloads\\dict\\data
for filename in os.listdir('C:\\Users\\andrey.melnik\\Downloads\\dict\\data'): # ['q.json']: # 
    print('filename=' + filename)
    with open('C:\\Users\\andrey.melnik\\Downloads\\dict\\data\\' + filename, 'r') as fp:
        obj = json.load(fp)
    continue   # check load dictionary
    #print(obj)
    # parse
    for x in obj:
        #print(x)
        #zealously
        wrd = obj.get(x)
        #print(wrd)
    #{'word': 'zealously', 'wordset_id': 'abcc065c2f', 'meanings': [{'id': '661371d17e', 'def': 'in a passionate manner', 'example': 'I worked zealously to raise funds for #the literacy project.', 'speech_part': 'adverb'}], 'editors': ['bryanedu', 'zellerpress'], 'contributors': ['sabreuse', 'malrase', 'lefurjah', 'msingle']}
        word = wrd.get('word')
        print('word=' + word)
        wordset_id = wrd.get('wordset_id')
        #print('wordset_id')
        #print(wordset_id)
        meaningslist = wrd.get('meanings')
        #print('meaningslist')
        #print(meaningslist)

        # few meanings
        # could be None
        if meaningslist == None: meanlen = 0
        else:  meanlen = len(meaningslist)
        for i in range(meanlen):
            #[{'id': '661371d17e', 'def': 'in a passionate manner', 'example': 'I worked zealously to raise funds for the literacy project.', 'speech_part': 'adverb'}]
            meaningsdict = meaningslist[i]
            id = meaningsdict.get('id')
            #print('id')
            #print(id)
            defn = meaningsdict.get('def')
            defn = defn[0:254]
            #print(defn)
            example = meaningsdict.get('example')
            #print(example)
            speech_part = meaningsdict.get('speech_part')
            #print(speech_part)
            synonyms = meaningsdict.get('synonyms')
            #print('synonyms=', synonyms)
            synonymst = synonyms
            if synonyms!=None:
                synonymst = '' # synonyms list as a string
                for syn in synonyms:
                    if syn!=None:
                        synonymst = synonymst + ', ' + syn
                synonymst = synonymst[0:254]

            sql = "INSERT INTO dct (word, wordset_id, id, defn, example, speech_part, synonyms) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (word, wordset_id, id, defn, example, speech_part, synonymst)
            #print('val=', val)
            mycursor.execute(sql, val)

            mydb.commit()

        #if True: break
    #if True: break

sql = "select count(*) from dct"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for s in myresult:
    print(s)


print('end')

