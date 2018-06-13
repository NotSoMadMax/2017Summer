import mysql.connector
import os


def CreateTable(table_name):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='test')
    cursor = cnx.cursor()
    sql = ("CREATE TABLE %s (Time VARCHAR(17))" % table_name)
    cursor.execute(sql)
    i = 1
    while i <= 512:
        name = 'value_%d' % i
        sql = "ALTER TABLE %s ADD %s DOUBLE" % (table_name,name)
        cursor.execute(sql)
        i += 1

    cnx.commit()
    cursor.close()
    cnx.close()


folder_list = []
source = '/Users/Max/Desktop/07/'
folder_list.append(source)
for root, dirs, files in os.walk(source):
    if root not in folder_list:
        folder_list.append(root)
        table_name = 'zjz2017' + folder_list[len(folder_list) - 1][19:21] + folder_list[len(folder_list) - 1][22:24]
        CreateTable(table_name)
