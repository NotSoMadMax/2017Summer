import xlrd
import mysql.connector

#print table.nrows,'*',table.ncols

#20170125_PUT.xls   1 columns
book = xlrd.open_workbook("20170125_PUT.xls")
table = book.sheet_by_index(0)
for rownum in range(table.nrows):
    row = table.row_values(rownum)
    t = ''
    for i in row:
        if type(i) == unicode:
            a = i.encode('ascii','ignore')
            t += a
        else:
            a = str(int(i))
            t += a

    cnx = mysql.connector.connect(user='root', password='1234',
                                  host='127.0.0.1',
                                  port=3306,
                                  database='test')
    cursor = cnx.cursor()

    cnx.commit()
    cursor.close()
    cnx.close()

#20170125_PUD.xls    28 columns
book = xlrd.open_workbook("20170125_PUD.xls")
table = book.sheet_by_index(0)
for rownum in range(table.nrows):
    row = table.row_values(rownum)
