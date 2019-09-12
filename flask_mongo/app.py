import os 
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import urllib.parse

app = Flask(__name__)

import pandas as pd 

df = pd.read_csv('creds.csv')
user = urllib.parse.quote_plus(df['User'][0])


client = MongoClient(f"mongodb+srv://<{user}>:<{df['Pass'][0]}>@cluster0-cu8yy.mongodb.net/test?retryWrites=true&w=majority")


db = client.tododb

@app.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)
    
@app.route('/new',methods = ['POST'])
def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one('todo')


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
