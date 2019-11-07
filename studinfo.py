import sqlite3
connection = sqlite3.connect("studinfo.db")
connection.execute("Create table student_information(ID int primary key not null, NAME text not null , AGE int not null, ADDRESS char(30) , CLASS int not null);")
print("CREATED")
connection.execute("INSERT INTO student_information(ID,NAME,AGE,ADDRESS,CLASS) VALUES(140, 'SAURAV',21,'TANDI',10)")
connection.execute("INSERT INTO student_information(ID,NAME,AGE,ADDRESS,CLASS) VALUES(132, 'SUTIHAL',84,'KOSHI',1)")
connection.execute("INSERT INTO student_information(ID,NAME,AGE,ADDRESS,CLASS) VALUES(130, 'CHUNGTA',20,'JAIPUR',16)")
connection.execute("INSERT INTO student_information(ID,NAME,AGE,ADDRESS,CLASS) VALUES(133, 'HARKE',21,'CHOLBASANTI NIWAS',11)")
connection.commit()
print("INFO INSERTED")
disp = connection.execute("SELECT ID,NAME,AGE,ADDRESS,CLASS FROM student_information")
for row in disp:
    print("-"*10) 
    print("ID=",row[0])
    print("NAME=",row[1])
    print("AGE=",row[2])
    print("ADDRESS=",row[3])
    print("CLASS=",row[4]),"\n"
print ("DISPLAYED DATA SUCCESSFULLY")

connection.execute("UPDATE student_information set NAME = 'MA' where id =140")
connection.commit()
disp = connection.execute("SELECT ID,NAME,AGE,ADDRESS,CLASS FROM student_information")
for row in disp:
    print("-"*10) 
    print("ID=",row[0])
    print("NAME=",row[1])
    print("AGE=",row[2])
    print("ADDRESS=",row[3])
    print("CLASS=",row[4]),"\n"
print ("UPDATED DATA SUCCESSFULLY")

connection.execute("DELETE from student_information where id =130")
connection.commit()
disp = connection.execute("SELECT ID,NAME,AGE,ADDRESS,CLASS from student_information")
for row in disp:
    print("-"*10) 
    print("ID=",row[0])
    print("NAME=",row[1])
    print("AGE=",row[2])
    print("ADDRESS=",row[3])
    print("CLASS=",row[4]),"\n"
print ("DELETED DATA SUCCESSFULLY")
connection.commit
connection.close()
