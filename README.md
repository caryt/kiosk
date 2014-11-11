Kiosk
=====

Sample Application using Flask / SQLAlchemy

Installation
------------
mkvirtualenv kiosk
pip install Flask
pip install flask-sqlalchemy
pip install pymysql
git clone "https://github.com/caryt/kiosk"
vi config.py #Edit SQLALCHEMY_DATABASE_URI as required
python kiosk.py

Browse to: localhost:5000

Run Tests
---------
python tests.py

