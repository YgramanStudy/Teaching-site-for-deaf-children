'''

#DataSourceSettings#
#LocalDataSource: MySQL for 5.1 - @localhost
#BEGIN#

<data-source source="LOCAL" name="MySQL for 5.1 - @localhost" uuid="96f91374-2dc6-424e-a885-9f5de9f603c0"><database-info product="MySQL" version="8.0.18-commercial" jdbc-version="4.0" driver-name="MySQL Connector Java" driver-version="mysql-connector-java-5.1.47 ( Revision: fe1903b1ecb4a96a917f7ed3190d80c049b1de29 )" dbms="MYSQL" exact-version="8.0.18" exact-driver-version="5.1"><extra-name-characters>#@</extra-name-characters><identifier-quote-string>`</identifier-quote-string></database-info><case-sensitivity plain-identifiers="lower" quoted-identifiers="lower"/><driver-ref>mysql</driver-ref><synchronize>true</synchronize><jdbc-driver>com.mysql.jdbc.Driver</jdbc-driver><jdbc-url>jdbc:mysql://localhost:3306</jdbc-url><secret-storage>master_key</secret-storage><user-name>root</user-name><schema-mapping><introspection-scope><node kind="schema" qname="new_schema"/></introspection-scope></schema-mapping></data-source>
#END#

'''

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Admin",
    database="mydatabase"

)


mycursor = mydb.cursor()

###mycursor.execute("CREATE DATABASE mydatabase")

###print(mydb)

###mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

###mycursor.execute("SHOW DATABASES")


###mycursor.execute("CREATE TABLE customers_1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")



###mycursor.execute("SHOW TABLES")


###for x in mycursor:
 ### print(x)



def Add_User(User_name,Password):

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (User_name, Password)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


###print("1 record inserted, ID:", mycursor.lastrowid)

def Get_User():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def Get_User_name():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT name FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)



def Get_User_PassWord():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT password FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)