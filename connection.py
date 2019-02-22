import mysql.connector

def connection():
    #connect to database
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='B@zinGa95',
        port=3306,
        database='movie_archive'
    )

    db_cursor = db.cursor()

    return db_cursor, db



