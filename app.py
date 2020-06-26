import os, flask_sqlalchemy 
from flask import Flask, render_template, request, jsonify,url_for 
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__) 
app.config.from_pyfile('config.py') #Bring All Configs from a Config File
db = SQLAlchemy(app)

from views import *
# @app.route("/") 
# def index():
#            return render_template('indexa.html')

# @app.route('/', methods=['POST'])
# def setchild():
#      fname = request.form['fname']
#      mname = request.form['mname']
#      lname = request.form['lname']
#      age = "age"
#      gender = request.form['gender']
#      dob = request.form['dateofbirth']
#      phone = request.form['phone']
#      community = request.form['community']
#      return render_template('newChild.html', fname=fname, dob=dob, lname = lname, age=age)

# @app.route("/",methods=['GET','POST'])
# def indexa():
#      search = 

# @app.route('/', methods=['POST'])
# def setparents():
#      fname = request.form['fname']
#      minitial = request.form['minitial']
#      lname = request.form['lname']
#      gender = request.form['gender']
#      phone = request.form['phone']
#      email =request.form['email']
#      return render_template('newChild.html', fname=fname, minitial=minitial, lname = lname, phone=phone, email=email)

# @app.route('/', methods=['POST'])
# def setworkers():
#      fname = request.form['fname']
#      minitial = request.form['minitial']
#      lname = request.form['lname']
#      gender = request.form['gender']
#      dob = request.form['dob']
#      age = "age"
#      phone = request.form['phone']
#      email =request.form['email']
#      return render_template('newChild.html', fname=fname, minitial=minitial, lname = lname, phone=phone, email=email)
     
# @app.route('/', methods=['POST'])
# def setworkers():
#      fname = request.form['fname']
#      minitial = request.form['minitial']
#      lname = request.form['lname']
#      gender = request.form['gender']
#      dob = request.form['dob']
#      age = "age"
#      phone = request.form['phone']
#      email =request.form['email']
#      return render_template('newChild.html', fname=fname, minitial=minitial, lname = lname, phone=phone, email=email)


if __name__ == "__main__":     
	app.run(debug=True, host=os.getenv("IP", 'localhost'),port=int(os.getenv("PORT", 5000) )) 