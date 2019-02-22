import mysql.connector
import xlrd
#connect to database
db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='B@zinGa95',
        port=3306,
        database='movie_archive'
)

db_cursor = db.cursor()


book = xlrd.open_workbook("Movie Archive.xlsx")
sheet = book.sheet_by_name("Total")
#insert excel files
query = (
        "INSERT INTO movies (Title, movie_format, owned, missing)"
        "VALUES (%s, %s, %s, %s)"
)

for r in range(2, sheet.nrows):
    name = (str(sheet.cell(r,1)))
    insert_data = False
    #parses and determines the titles for movies with special characters
    if "number" in name:
        #turns titles with only numbers to text
        num_name = name.split(':')
        name = "'"+str(int(float(num_name[1])))+"'"
        insert_data = True
    elif "text" in name and len(name)<30:
        str_name = name.split(':u')
        name = str_name[1]
        insert_data = True
    
    owned = (str(sheet.cell(r,2))).split(":")
    format_type = (str(sheet.cell(r,3))).split(":u")
    missing = (str(sheet.cell(r,4))).split(":")

    if insert_data == True:
        data = (name, format_type[1], owned[1], missing[1])
        db_cursor.execute(query,data)

db_cursor.close()
db.commit()
db.close()

