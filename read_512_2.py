import mysql.connector
import time
import os


def CreateTable(table_name):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='zjz')
    cursor = cnx.cursor()

    sql = "CREATE TABLE IF NOT EXISTS `%s` (Time VARCHAR(17), " % table_name
    for i in range(1, 512):
        sql += "value_{} DOUBLE, ".format(i)
    sql += "value_512 DOUBLE, UNIQUE (Time))"    # set Time unique for duplicates check

    cursor.execute(sql)

    cnx.commit()
    cursor.close()
    cnx.close()


def InsertNew(file_name, table_name):
    fhand = open(file_name)
    time = file_name.split('.txt')[0][-6:] # '/Users/Max/Desktop/07/01/20170701000026.txt' -> 000026

    data = list()
    data.append(time)

    number = fhand.readline().split(' ')

    for n in number:
        if n != '':
            data.append(float(n))

    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='zjz')
    cursor = cnx.cursor()

    add = ("INSERT IGNORE INTO {} VALUES "     # ignore when duplicate
           "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)").format(table_name)

    cursor.execute(add, data)
    cnx.commit()
    cursor.close()
    cnx.close()


def createList():               # create two lists to store inserted file and folder names
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='zjz')

    cursor = cnx.cursor()

    folder_list = "CREATE TABLE IF NOT EXISTS FolderList (FolderName VARCHAR(50), UNIQUE (FolderName))"
    file_list = "CREATE TABLE IF NOT EXISTS FileList (FileName VARCHAR(50), UNIQUE (FileName))"

    cursor.execute(folder_list)
    cursor.execute(file_list)

    cnx.commit()
    cursor.close()
    cnx.close()

def addToFolderList(folder):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='zjz')
    cursor = cnx.cursor()
    add = "INSERT IGNORE INTO FolderList (FolderName) VALUES " \
          "(%s)" % folder
    cursor.execute(add)
    cnx.commit()
    cursor.close()
    cnx.close()


def copyList():
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='zjz')
    cursor = cnx.cursor()


if __name__ == "__main__":
    createList()
    file_list = []
    folder_list = []

    source = '/Users/Max/Desktop/2017Summer/data/2017/'
    addToFolderList(source)
    flag = True     # flag is for test purpose only, delete this flag when using time.sleep method
    table_name = ''

    while flag:

        for month in os.listdir(source):
            if month.startswith("."):
                continue

            for day in os.listdir(os.path.join(source, month)):
                if day.startswith("."):
                    continue
                if day.startswith("_"):
                    continue
                if os.path.join(source, month, day) not in folder_list:
                    addToFolderList(os.path.join(source, month, day))
                    table_name = 'zjz2017{}{}'.format(month, day)
                    CreateTable(table_name)
                    print 'table ', table_name, 'created'       # for debugging

                for file in os.listdir(os.path.join(source, month, day)):
                    if file.startswith("."):
                        continue
                    if os.path.join(source, month, day, file) not in file_list:
                        InsertNew(os.path.join(source, month, day, file), table_name)
                        file_list.append(os.path.join(source, month, day, file))
                        print os.path.join(source, month, day, file), 'inserted'    # for debugging
        # flag = False
        time.sleep(10)
