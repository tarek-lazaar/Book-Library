from flask import Flask, render_template, request , redirect

import pymysql

app = Flask(__name__,template_folder='templates')



conn = pymysql.connect(
    host='database-1.cmcycie0rurf.eu-west-3.rds.amazonaws.com',
    port=3306,
    user='admin',
    password='ttllzz00',
    db='Library',

)


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/addbook")
def welcome():
    return render_template('addbook.html')

@app.route("/findbook")
def find():
    return render_template('findbook.html')

@app.route("/data" , methods=['POST'])
def data():
    book_name = request.form["Book"]
    author_name = request.form["Author"]
    book_year = request.form["Year"]
    book_genre = request.form["Genre"]
    cur = conn.cursor()
    cur.execute("REPLACE INTO Books (name,author,Year,Genre) VALUES (%s,%s,%s,%s)",
                (book_name, author_name, book_year,book_genre))
    conn.commit()
    return "<h1> Book added to the database </h1>"

@app.route("/findata" , methods=['POST'])
def findata():
    book_name = request.form["Book"]
    author_name = request.form["Author"]
    cur = conn.cursor()
    if book_name != "":
        row = cur.execute("SELECT * FROM  Books WHERE  name = %s",
                    (book_name,))
        rows = cur.fetchall()
        result = [rows[0][0] ,rows[0][1] , rows[0][2] , rows[0][3]]
        return render_template("Bookview.html" , result=result)
    elif author_name != "":
        row = cur.execute("SELECT * FROM  Books WHERE  author = %s",
                          (author_name,))
        rows = cur.fetchall()
        result = [rows[0][0], rows[0][1], rows[0][2], rows[0][3]]
        return render_template("Bookview.html", result=result)

    else :
        return "Enter Book or author name please"


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")