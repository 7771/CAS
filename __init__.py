from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'some$3cretKey' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:// zoe:password@localhost/db' 

db = SQLAlchemy(app) 

from app import views, models