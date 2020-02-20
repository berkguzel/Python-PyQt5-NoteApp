import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from notes import notes
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore
import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient
import pprint

class myApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myApp, self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pb_add.clicked.connect(self.addArticle)
        self.ui.pb_edit.clicked.connect(self.editArticle)
        self.ui.pb_search.clicked.connect(self.searchingArticle)
        self.ui.pb_delete_2.clicked.connect(self.removeArticle)
        self.ui.pb_delete_3.clicked.connect(self.removeResults)
        self.ui.pb_markasRead.clicked.connect(self.markasRead)
        self.ui.pb_search_2.clicked.connect(self.readAnalysis)
        self.loadUnreadTags()
        
        self.ui.pb_exit.clicked.connect(self.reset)
        self.loadArticles()

    def loadUnreadTags(self):
        myclient= pymongo.MongoClient("mongodb+srv://berkguzel:yxp6x9kqwvFxAsbn@cluster0-feifa.mongodb.net/test?retryWrites=true&w=majority")
        mydb=myclient["notes-py"]
        mycollection=mydb["notes"]
        mycollection1=mydb["tags"]

        for i in mycollection1.find({}):  
            self.ui.list_analysis.addItem(i["name"]+" = "+str(i["unreadcount"]))


    def reset(self):
        myclient= pymongo.MongoClient("mongodb+srv://berkguzel:yxp6x9kqwvFxAsbn@cluster0-feifa.mongodb.net/test?retryWrites=true&w=majority")
        mydb=myclient["notes-py"]
        mycollection1=mydb["tags"]
        
        for i in mycollection1.find({}):
            reset=i["name"]
            mycollection1.update_one({"name":reset},{"$set":{"count":0}})

    def readAnalysis(self):
        newArticle=notes()
        newArticle.analysis()

    def markasRead(self):
        myclient= pymongo.MongoClient("mongodb+srv://berkguzel:yxp6x9kqwvFxAsbn@cluster0-feifa.mongodb.net/test?retryWrites=true&w=majority")
        mydb=myclient["notes-py"]
        mycollection=mydb["notes"]
        mycollection1=mydb["tags"]

        index=self.ui.list_addedToday.currentRow()
        item=self.ui.list_addedToday.item(index)

        question=QMessageBox.question(self, "Mark as Read Article", "Chosen Article will be mark as read. Are you sure?",QMessageBox.Yes|QMessageBox.No)

        if question==QMessageBox.Yes:
            item=self.ui.list_addedToday.takeItem(index)
            filter={"article":item.text()}
            result=mycollection.find(filter)

            for i in result:
                message=i["tags"]

            for k in message:
                filter={"name":k}
                result=mycollection1.find(filter)
                for i in result:
                    count=i["count"]+1
                    unreadcount=i["unreadcount"]-1
                    mycollection1.update_one({"name":k},{"$set":{"unreadcount":unreadcount}})
                    mycollection1.update_one({"name":k},{"$set":{"count":count}})
                    mycollection.delete_one({"article":item.text()})
                    del item
                    self.ui.list_analysis.clear()
                    self.loadUnreadTags()


    def removeResults(self):
        self.ui.list_results.clear()
        
    def searchingArticle(self):
        myclient= pymongo.MongoClient("mongodb+srv://berkguzel:yxp6x9kqwvFxAsbn@cluster0-feifa.mongodb.net/test?retryWrites=true&w=majority")
        checkedList=[]
        mydb=myclient["notes-py"]
        mycollection=mydb["notes"]
        count=0
        items=self.ui.groupBox_adding.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if(cb.isChecked()==True):
                checkedList.append(cb.text())
                count=count+1

        if count!=6:
            for item in checkedList:
                filter={"tags":item}
                result=mycollection.find(filter)
                for i in result:
                    self.ui.list_results.addItem(i["article"])
                for cb in items:
                    if(cb.isChecked()):
                        cb.setChecked(False)

        if count==6:
            for i in mycollection.find({},{"article":1,"_id":0}):
                self.ui.list_results.addItem(i["article"])
            
    def removeArticle(self):


        myclient= pymongo.MongoClient("mongodb+srv://berkguzel:yxp6x9kqwvFxAsbn@cluster0-feifa.mongodb.net/test?retryWrites=true&w=majority")
        mydb=myclient["notes-py"]
        mycollection=mydb["notes"]
        mycollection1=mydb["tags"]

        index=self.ui.list_addedToday.currentRow()
        item=self.ui.list_addedToday.item(index)

        question=QMessageBox.question(self, "Remove Article", "Chosen Article will be removed. Are you sure?",QMessageBox.Yes|QMessageBox.No)

        if question==QMessageBox.Yes:
            item=self.ui.list_addedToday.takeItem(index)
            filter={"article":item.text()}
            result=mycollection.find(filter)


            for i in result:
                message=i["tags"]

            for k in message:
                filter={"name":k}
                result=mycollection1.find(filter)
                for i in result:
                    unreadcount=i["unreadcount"]-1
                    mycollection1.update_one({"name":k},{"$set":{"unreadcount":unreadcount}})
                    self.ui.list_analysis.clear()
                    self.loadUnreadTags()
            mycollection.delete_one({"article":item.text()})
            del item
    
    def addArticle(self):
        myclient= pymongo.MongoClient("mongodb+srv://berkguzel:yxp6x9kqwvFxAsbn@cluster0-feifa.mongodb.net/test?retryWrites=true&w=majority")
        mydb=myclient["notes-py"]
        mycollection=mydb["notes"]
        mycollection1=mydb["tags"]
        newArticle=notes()
        items=self.ui.groupBox_adding.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if(cb.isChecked()):
                newArticle.tags.append(cb.text())
                filter={"name":cb.text()}
                result=mycollection1.find(filter)
                for i in result:
                    count=i["unreadcount"]+1
                    mycollection1.update_one({"name":cb.text()},{"$set":{"unreadcount":count}})

        if(len(newArticle.tags)==0):
            question=QMessageBox.question(self, "TAGS WERE NOT CHOOSEN", "You must be choose tags firstly!",QMessageBox.Ok)
        
        else:
            text, okPressed = QInputDialog.getText(self, "Get Article","Article message:", QLineEdit.Normal, "")
            if okPressed and text != '':
                self.ui.list_analysis.clear()
                self.loadUnreadTags()
                self.ui.list_addedToday.addItem(text)

                product={"article":text, "tags":newArticle.tags}
                x=mycollection.insert_one(product)
                newArticle.tags.clear()

                for cb in items:
                    if(cb.isChecked()):
                        cb.setChecked(False)
    
    def editArticle(self):
        index=self.ui.list_addedToday.currentRow()
        item=self.ui.list_addedToday.item(index)

        if item is not None:
            text, ok=QInputDialog.getText(self, "Edit Article", "Article Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)

    def loadArticles(self):
        myclient= pymongo.MongoClient("mongodb+srv://berkguzel:yxp6x9kqwvFxAsbn@cluster0-feifa.mongodb.net/test?retryWrites=true&w=majority")
        mydb=myclient["notes-py"]
        mycollection=mydb["notes"]
        for i in mycollection.find({},{"article":1,"_id":0}):
            self.ui.list_addedToday.addItem(i["article"])
           
    def searchingTags(self):
        searchingArticle=notes()
        items=self.ui.groupBox_searching.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if(cb.isChecked()):
                searchingArticle.searchingTags.append(cb.text())

def app():
    app=QtWidgets.QApplication(sys.argv)
    win=myApp()
    win.show()
    sys.exit(app.exec_())

app()
