import mysql.connector
import time
import datetime
import os


def addToFolderList(folder):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='zjz')
    cursor = cnx.cursor()

    add = ("INSERT INTO FolderList "
           "(FolderName) VALUES ({})").format(folder)

    cursor.execute(add)
    cnx.commit()
    cursor.close()
    cnx.close()


a = "users"
print type(a)
addToFolderList(a)



'''
source = '/Users/Max/Desktop/2017Summer/data/2017/'

for month in os.listdir(source):
    if month.startswith("."):
        continue

    for day in os.listdir(os.path.join(source, month)):
        if day.startswith("."):
            continue
        if day.startswith("_"):
            continue
        addToFolderList(os.path.join(source, month, day))
'''