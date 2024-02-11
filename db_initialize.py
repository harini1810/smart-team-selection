import sqlite3

connection=sqlite3.connect("Customers.db")
cursor=connection.cursor()

cursor.execute("DROP TABLE CUSTOMER;")

sql_query='''CREATE TABLE CUSTOMER(
                NAME VARCHAR(20) NOT NULL,
                MAIL VARCHAR(30) NOT NULL,
                PHONE NUMBER PRIMARY KEY,
                PWD VARCHAR(15) NOT NULL);'''
cursor.execute(sql_query)

sql_query='''INSERT INTO CUSTOMER VALUES
                ('admin','admin@gmail.com',9876543210,'admin');'''
cursor.execute(sql_query)

print("success")
connection.commit()
cursor.execute("DROP TABLE EMPLOYEE")
sql_query='''CREATE TABLE EMPLOYEE(
                NAME VARCHAR(20) NOT NULL,
                MAIL VARCHAR(30) NOT NULL,
                COMPANY VARCHAR(30) NOT NULL,
                ID VARCHAR(15) NOT NULL,
                JAVA INT,
                PYTHON INT,
                JAVASCRIPT INT,
                HTML INT,
                CSS INT,
                DJANGO INT,
                CPP INT,
                MONGODB INT,
                PHP INT,
                NODEJS INT,
                REACT INT,
                ANGULARJS INT,
                DSA INT,
                FLASK INT,
                MYSQL INT);'''
cursor.execute(sql_query)
sql_query='''INSERT INTO EMPLOYEE VALUES(
'Ram','ram@gmail.com','admin','E001',1,1,1,0,0,0,0,0,0,1,1,0,0,0,0
)'''
cursor.execute(sql_query)

sql_query='''INSERT INTO EMPLOYEE VALUES(
'Shiva','shiva@gmail.com','admin','E002',1,0,1,0,0,0,0,1,1,0,0,1,0,0,0
)'''
cursor.execute(sql_query)

sql_query='''INSERT INTO EMPLOYEE VALUES(
'Krish','krish@gmail.com','admin','E003',1,1,1,0,0,0,0,0,0,1,1,0,0,0,0
)'''
cursor.execute(sql_query)

sql_query='''INSERT INTO EMPLOYEE VALUES(
'Neha','neha@gmail.com','admin','E004',0,1,1,0,0,0,1,0,0,1,1,0,0,1,0
)'''
cursor.execute(sql_query)

sql_query='''INSERT INTO EMPLOYEE VALUES(
'Vicky','vivcky@gmail.com','admin','E005',0,0,1,0,1,0,0,1,0,1,0,0,1,0,1
)'''
cursor.execute(sql_query)


sql_query='''SELECT NAME,MAIL,PHONE,PWD FROM CUSTOMER'''
cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()