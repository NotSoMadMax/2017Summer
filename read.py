import mysql.connector
import time
import os


def InsertNew(file_name):
    if len(file_name) != 61: return
    fhand = open(file_name)
    time = file_name[40:57]
    cnx = mysql.connector.connect(user='myuser', password='mypassword',
                                  host='158.132.126.193',
                                  port=6666,
                                  database='hst')
    cursor = cnx.cursor()
    for line in fhand:
        line = line.rstrip()
        data = line.split(',')
        if len(data) == 4:
            sliced_data = []
            for n in data:
                a = ''
                x = n.split('\0')
                for i in x: a += i
                sliced_data.append(a)

            add = ("INSERT INTO test "
                    "(name1, name2, name3, value, time) "
                    "VALUES (%s, %s, %s, %s, %s)")
            add_data = (sliced_data[0],sliced_data[1],sliced_data[2],sliced_data[3],time)
            cursor.execute(add,add_data)
    cnx.commit()
    cursor.close()
    cnx.close()


file_list = []
flag = True
while flag:
    #source = raw_input('Please enter root directory:')
    source = '/Users/Max/Desktop/201604/2016-04-17/'
    for root, dirs, files in os.walk(source):
        for name in files:
            file = os.path.join(root, name)
            if file not in file_list:
                InsertNew(file)
                file_list.append(file)
            else : flag = False
    #time.sleep(10)
