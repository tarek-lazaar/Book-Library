from flask import Flask, render_template, request , redirect
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__,template_folder='templates', instance_relative_config=False)

app.config.from_object(Config)

db = SQLAlchemy(app)

#database Model

class Books(db.Model):
    __tablename__ = 'Books'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=200))
    author = db.Column(db.VARCHAR(length=200))
    Year = db.Column(db.Integer)
    Genre = db.Column(db.VARCHAR(length=255))




@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/addbook")
def welcome():
    return render_template('addbook.html')

@app.route("/findbook")
def findbook():
    return render_template('findbook.html')

@app.route("/deletebook")
def delete():
    return render_template('deletebook.html')

#add new book to the Library database
@app.route("/data" , methods=['POST'])
def data():
    book_name = request.form["Book"]
    author_name = request.form["Author"]
    book_year = request.form["Year"]
    book_genre = request.form["Genre"]
    new_book = Books(name=book_name, author=author_name, Year=book_year, Genre=book_genre)
    db.session.add(new_book)
    db.session.commit()

    return "<h1> Book added to the database </h1>"

#searching books with book name or author name
@app.route("/findata" , methods=['POST'])
def findata():
    book_name = request.form["Book"]
    author_name = request.form["Author"]

    if book_name != "":
        book = Books.query.filter_by(name=book_name).first() # select * where name = book_name
        if book is not None : #check if book exists
            result = [book.name , book.author , book.Year , book.Genre]
            return render_template("Bookview.html" , result=result)
        else :
            return "Book not found"
    elif author_name != "":
        book = Books.query.filter_by(author=author_name).first()
        if book is not None : #check if book exists
            result = [book.name, book.author, book.Year, book.Genre]
            return render_template("Bookview.html", result=result)
        else :
            return "Book not found"

    else :
        return "Enter Book or author name please"

#delete book from database

@app.route("/deletebook", methods=['POST'])
def deletebook():
    book_name = request.form["Book"]
    result = Books.query.distinct(Books.name)
    titles = [r.name for r in result]
#check if the book exists
    if book_name in titles :
        db.session.query(Books).filter(Books.name == book_name).delete()
        db.session.commit()
        return "Book deleted"

    else:

        return "Book not found"




if __name__ == '__main__':
    app.run(debug=True , port=5000 , host='0.0.0.0')