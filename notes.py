import matplotlib.pyplot as plt
import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient

class notes():
    tags=[]
    name=[]
    countList=[]
    searchingTags=[]
    color=["#FFCCCC","#00CCCC","#CC0000","#00994C","#994C00","#A0A0A0"]
    tags_types="Software","Cloud Native, AWS","Science","Technology","Python, ML, Data Science","Others"

    def __init__(self):
        pass


    def analysis(self):
        myclient= pymongo.MongoClient("mongodb connection url")
        mydb=myclient["notes-py"]
        mycollection=mydb["notes"]
        mycollection1=mydb["tags"]
        for i in mycollection1.find({},{"name":1,"_id":0,"count":1}):
            self.countList.append(i["count"])

        plt.pie(self.countList,colors=self.color,labels=self.tags_types, shadow=True, explode=(0.05,0.05,0.05,0.05,0.05,0.05), autopct="%1.1f%%")
        plt.show()
            

            

    

    


