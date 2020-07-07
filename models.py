from app import db 

class Room(db.Model):     
    rid = db.Column(db.Integer, primary_key=True)     
    capacity = db.Column(db.String(80))     
    gender = db.Column(db.String(120)) 
    facilities = db.Column(db.String(200))
    room_parents = db.Column(db.Integer)
    room_score = db.Column(db.Integer)
   

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
    
class Parent(db.Model):
    parent_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname= db.Column(db.Integer, db.ForeignKey('user.user_id'))
    phone = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    email = db.Column(db.String)
    gender = db.Column(db.Boolean)
    skills = db.Column(db.String(100))

    def __init__(self, capacity, gender, facilities):         
        self.capacity = capacity         
        self.gender = gender
        self.facilities = facilities
    
    def __repr__(self):
        return '<User %r>' % self.rid
    
