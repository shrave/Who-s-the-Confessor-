# import csv
# import mysql.connector

# mydb = mysql.connector.connect(host='localhost',
#	 user='root',
#	 passwd='13114214522',
#	 db='IIIT_STUDENTS')
# cursor = mydb.cursor()

# csv_data = csv.reader(file('full2.csv'))
# for i in csv_data:
# 	print i

# cursor.execute("CREATE TABLE All_data (program VARCHAR(255), batch VARCHAR(255), branch VARCHAR(255), firstname VARCHAR(255), lastname VARCHAR(255))")


# for row in csv_data:
#	 cursor.execute('INSERT INTO All_data(program, batch, branch, firstname, lastname)' \
#		   'VALUES("%s", "%s", "%s", "%s", "%s")',
#		   tuple(row))
	

# #close the connection to the database.
# mydb.commit()
# cursor.close()
# print "Done"





import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
	user='root',
	passwd='13114214522',
	db='IIIT_STUDENTS')
cursor = mydb.cursor()
count = 0
csv_data = csv.reader(file('full2.csv'))
for row in csv_data:
	print row
	cursor.execute('INSERT INTO All_data(program, batch, branch, firstname, lastname)' \
		  'VALUES("%s", "%s", "%s","%s","%s")', 
		  row)
	count += 1
#close the connection to the database.
print count
mydb.commit()
cursor.close()
print "Done"