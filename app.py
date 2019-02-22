from flask import Flask, render_template, flash, redirect, request, session, abort
from connection import connection

#start application
app = Flask(__name__)

#http:localhost/
@app.route("/", methods = ["GET", "POST"])
def main():
    #install index page
    try:
        cursor, database = connection()
    except Exception as e:
        print("Error returned:",str(e))
    return render_template('home.html')
'''
#http:localhost/page1
@app.route("/page1")
def page():
    #install page 1
    return render_template('page1.html')
'''
if __name__ == "__main__":
    #run application
    app.run()



