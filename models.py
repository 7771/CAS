from flask import Flask
from . import db
 
"""engine = create_engine('sqlite:///')
conn = engine.connect()"""

class Child(db.Model):
    child_id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    dob = db.Column(db.Date)
    fname = db.Column(db.String(25))
    lname = db.Column(db.String(30))
    mname = db.Column(db.String(30))
    parentname = db.Column(db.String(50))
    illness = db.Column(db.String(100))
    mentor_comment = db.Column(db.String(250))
    nurse_comment = db.Column(db.String(250))
    phone = db.Column(db.Integer)
    gender = db.Column(db.Boolean, default = True)
    parent = db.Column(db.String, db.ForeignKey('parent.parent_id'))
    room_score = db.Column(db.Integer)

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return '<Child %r>' % self.fname
#####customize gender booleans

class Worker(db.Model):
    worker_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25))
    mname = db.Column(db.String(25))
    lname = db.Column(db.String(30))
    gender = db.Column(db.Boolean, default=True)
    event = db.Column(db.String(30))
    event_year= db.Column(db.Date)
    age = db.Column(db.Integer)
    location = db.Column(db.String(50))
    nurse = db.Column(db.Boolean, default=False)
    parent = db.Column(db.Boolean, default=False)
    #creator = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    
class Parent(db.Model):
    parent_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname= db.Column(db.Integer, db.ForeignKey('user.user_id'))
    phone = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    email = db.Column(db.String)
    gender = db.Column(db.Boolean)
    skills = db.Column(db.String(100))

class Rooms(db.Model):
    room_id = db.Column(db.Integer, primary_key=True)
    room_score = db.Column(db.Integer)
    room_bathrooms = db.Column(db.Integer)
    room_gender = db.Column(db.Boolean)
    room_beds = db.Column(db.Integer)
    room_parents = db.Column(db.Integer)

