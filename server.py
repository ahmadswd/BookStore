from flask import Flask
from flask import Flask, request, url_for, redirect, render_template
from pymongo import MongoClient

app = Flask(__name__)
connection = MongoClient()
db = connection.BookStore #database name.
collection = db.Books # collection name.



@app.route('/')
def hello():
     return render_template('index.html')

@app.route('/new', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':    
        isbn_h = request.form['isbn']
        b_title_h = request.form['name']
        b_author_h = request.form['author']
        db.Books.insert({'isbn': isbn_h, 'book_n': b_title_h,'book_a':b_author_h})
        
        return redirect(url_for('hello'))

    return render_template('new.html')

   
if __name__ == '__main__':
    app.run()