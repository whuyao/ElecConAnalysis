#coding=gbk
import json
import os
import time
import csv
import pymongo

def ger_data(_id):
    myquery={"_id":_id}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
    return x
        

def import_csv(name):
    power_id=[]
    with open(name, "r", encoding="utf-8") as csvfile:
       reader = csv.reader(csvfile)
       data = [row for row in reader]
       data_rows=len(data)-1
       for i in range(data_rows):
           power_id.append(data[i+1][3])
    return power_id
          
    
if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient["jxpower"]
    mycol = mydb["power_test_result"]
    
    _id=129786
    data=ger_data(_id)
    print(data)
    
    
    name="2018.csv"
    power_id=import_csv(name)
    

