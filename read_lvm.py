import mysql.connector
import time


def CreateTable(table_name):

    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='test')
    cursor = cnx.cursor()
    sql = "CREATE TABLE IF NOT EXISTS {} (Time VARCHAR(30), Point_1 INT(11), Band_1 INT(11), Point_2 INT(11)," \
          "Band_2 INT(11), Point_3 INT(11), Band_3 INT(11), Point_4 INT(11), Band_4 INT(11), Point_5 INT(11), " \
          "Band_5 INT(11), UNIQUE (Time))" .format(table_name)

    cursor.execute(sql)
    cnx.commit()
    cursor.close()
    cnx.close()


def InsertNew(record, table_name):
    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='test')
    cursor = cnx.cursor()

    add = ("INSERT IGNORE INTO {} VALUES "
           "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)").format(table_name)

    cursor.execute(add, record)
    cnx.commit()
    cursor.close()
    cnx.close()



if __name__ == "__main__":

    table_list = list()

    fhand = open('/Users/Max/Desktop/170619.lvm')
    for line in fhand:                              # read and store existing data
        data = line.split()
        Time = ''
        day = ''
        for i in data[0].split('/'):                # data[0] --> 2017/6/21
            Time += i
            day += i
        for i in data[1].split(':'):                # data[1] --> 11:55:49
            Time += i

        table_name = 'LabView{}'.format(day)
        if table_name not in table_list:
            CreateTable(table_name)
            table_list.append(table_name)

        record = list()
        record.append(Time)
        for i in range(2, 12):
            record.append(int(data[i]))
        InsertNew(record, table_name)

    while True:                                     # insert the last record every 5s
        fh = open('/Users/Max/Desktop/170619.lvm')  # read the last line
        data = (fh.readlines()[-1]).split()
        Time = ''
        day = ''
        for i in data[0].split('/'):
            Time += i
            day += i
        for i in data[1].split(':'):
            Time += i

        table_name = 'LabView{}'.format(day)
        if table_name not in table_list:
            CreateTable(table_name)
            table_list.append(table_name)

        record = list()
        record.append(Time)
        for i in range(2, 12):
            record.append(int(data[i]))
        InsertNew(record, table_name)
        print '{} inserted'.format(Time)
        time.sleep(5)

