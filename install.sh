#! /bin/bash
sudo yum update
sudo yum install git
pip install flask
pip install mysqlclient
pip install Flask-SQLAlchemy
cd ~
git clone https://github.com/tarek-lazaar/Book-Library.git
cd  Book-Library/
export SECRET_KEY=ttllzz00
pyhton app.py

