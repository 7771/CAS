from app.models import Room, Worker, Child
from app import db 

child = Child('admin', 'admin@example.com') 
worker = Worker('guest', 'guest@example.com') 
room = Room('')

db.session.add(child) 

db.session.commit()
db.session.query(Child).all() 

#db.session.add(worker) 
#db.session.add(room)
