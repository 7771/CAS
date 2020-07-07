from views import db

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
    parent = db.Column(db.String (50), db.ForeignKey('parent.parent_id'))
    location = db.Column(db.String(50))

    def __init__(self, fname, lname, age, mname, dob, parentemail, illness, phone, gender, location):
        self.fname = fname
        self.lname = lname
        self.mname = mname
        self.age = age
        self.dob = dob
        self.parentemail = parentemail
        self.illness = illness
        self.phone = phone
        self.gender = gender
        self.location = location
        

    def get_id(self):
        try:
            return unicode(self.child_id)  # python 2 support
        except NameError:
            return str(self.child_id)  # python 3 support
    
class Worker(db.Model):
    
    worker_email = db.Column(db.String(35), primary_key=True)
    fname = db.Column(db.String(25))
    mname = db.Column(db.String(25))
    lname = db.Column(db.String(30))
    gender = db.Column(db.Boolean, default=True)
    age = db.Column(db.Integer)
    event_id = db.Column(db.String(30))
    location = db.Column(db.String(50))
    nurse = db.Column(db.Boolean, default=False)
    parent = db.Column(db.Boolean, default=False)
    dob = db.Column(db.Date)
    
    def __init__(self,worker_email, fname, mname, lname, age, gender, location,nurse,dob):
        self.worker_email = worker_email
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.gender = gender
        self.location = location
        self.nurse = nurse
        self.dob = dob
        self.age = age
    
    # def __repr__(self):
    #     return '<Worker %r>' % self


class Parent(db.Model):
    parent_email = db.Column(db.String(35), primary_key=True)
    fname = db.Column(db.String(15))
    lname= db.Column(db.Integer, db.ForeignKey('user.user_id'))
    phone = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    gender = db.Column(db.Boolean)

    def __init__(self,parent_email, fname, lname, phone, gender):
        self.parent_email = parent_email
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.gender = gender
    
class Rooms(db.Model):
    room_no = db.Column(db.Integer, primary_key=True)
    room_capacity = db.Column(db.Integer)
    room_parent = db.Column(db.Integer)
    room_children = db.Column(db.String)
    room_gender = db.Column(db.String)

    def __init__(self,room_no, room_capacity, room_parent, room_children, room_gender):
        self.room_no = room_no
        self.room_capacity = room_capacity
        self.room_parent =room_parent
        self.room_children = room_children
        self.room_gender = room_gender
        
    
class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_name =db.Column(db.String(15))
    event_year = db.Datedate(db.Date)
    event_registered = db.Column(db.String)

    def __init__(self, event_id, event_name, event_year, event_registered):
        self.event_id = event_id
        self.event_name = event_name
        self.event_year = event_year
        self.event_registered = event_registered
        

    # def event_id():
    #     return self.event_id
    
    # def event_name():
    #     return self.event_name

    # def event_year():
    #     return self.event_year
