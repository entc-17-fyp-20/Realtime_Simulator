import mysql.connector


def connect_db():
    mydb = mysql.connector.connect(host="localhost", user="root", database="condition1", )
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE error_table")
    mycursor.execute("CREATE TABLE error_table (id INT AUTO_INCREMENT PRIMARY KEY, datetime DATETIME, predicted FLOAT(12,6), actual FLOAT(12,6), difference FLOAT(12,6))")
    return mydb


def insert_db(mydb, predicted, actual, difference):
    mycursor = mydb.cursor()

    sql = "INSERT INTO error_table(datetime, predicted, actual, difference) VALUES (NOW(), %s, %s, %s)"
    val = (predicted, actual, difference)
    mycursor.execute(sql, val)

    # mycursor.execute("SELECT * FROM error_table")
    #
    # myresult = mycursor.fetchall()
    #
    # for x in myresult:
    #     print(x)
    #

    mydb.commit()
