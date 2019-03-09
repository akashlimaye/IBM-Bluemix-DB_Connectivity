import os
from flask import Flask,redirect,render_template,request,random
import urllib
import datetime
import json
import pypyodbc
import time

app = Flask(__name__)

server = 'akashlimaye.database.windows.net'
database = 'myDB'
username = 'akashlimaye'
password = 'Summerof69'
driver= '{ODBC Driver 13 for SQL Server}'

@app.route('/')
def index():
    return render_template('index.html')     
# return render_template("list.html",rows=rows)

@app.route('/lookup', methods=['GET'])
def dispdata():
    a = request.args.get('val1')
    b = request.args.get('val2')
    dbconn = pypyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = dbconn.cursor()
    start = time.time()
    for x in range(0, 100):
        val = random.uniform(a,b)
        cursor.execute("SELECT * from [EARTHQUAKE] where mag<'"+val+"'")
    end = time.time()
    duration = end - start
    return render_template('list.html', dur=duration)

if __name__ == '__main__':
    app.run(debug = True)