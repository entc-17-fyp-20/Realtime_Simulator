import mysql.connector


def power_last_30():
    mydb = mysql.connector.connect(host="localhost", user="root", database="condition1")
    mycursor = mydb.cursor()

    query = "SELECT * FROM warning_table ORDER BY id DESC LIMIT 30"

    mycursor.execute(query)
    data = mycursor.fetchall()

    # Connections should be closed before returning
    mycursor.close()
    mydb.close()
    return data

def power_last():
    mydb = mysql.connector.connect(host="localhost", user="root", database="condition1")
    mycursor = mydb.cursor()

    query = "SELECT * FROM warning_table ORDER BY id DESC LIMIT 1"

    mycursor.execute(query)
    data = mycursor.fetchall()

    # Connections should be closed before returning
    mycursor.close()
    mydb.close()
    return data


def condition_last_30():
    mydb = mysql.connector.connect(host="localhost", user="root", database="condition1")
    mycursor = mydb.cursor()

    query = "SELECT * FROM error_table ORDER BY id DESC LIMIT 30"

    mycursor.execute(query)
    data = mycursor.fetchall()

    # Connections should be closed before returning
    mycursor.close()
    mydb.close()
    return data

def condition_last():
    mydb = mysql.connector.connect(host="localhost", user="root", database="condition1")
    mycursor = mydb.cursor()

    query = "SELECT * FROM error_table ORDER BY id DESC LIMIT 1"

    mycursor.execute(query)
    data = mycursor.fetchall()

    # Connections should be closed before returning
    mycursor.close()
    mydb.close()
    return data

