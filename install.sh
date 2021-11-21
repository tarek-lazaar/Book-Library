#! /bin/bash
sudo yum install git -y
sudo yum install python2 -y
sudo yum install python2-pip -y
sudo pip2 install flask
sudo pip2 install Flask-SQLAlchemy
sudo alternatives --set python /usr/bin/python2
touch ~/test.txt
git clone https://github.com/tarek-lazaar/Book-Library.git ~/Book-Library
export SECRET_KEY=ttllzz00
python ~/Book-Library/app.py
