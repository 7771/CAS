from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify 
import uuid, jwt, datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from modelss import *

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-auth-token' in request.headers:
            token = request.headers['x-auth-token']

        
        if not token:
            return jsonify({'message': 'Token is missing!'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            
            current_user = Worker.query.filter_by(
                public_id=data['id']).first()
            
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/person')
def get_child(child_id):
    first_user = Child.query.filter_by(child_id=child_id).first()
    return "fname: {}, lname:{}".format(first_user.fname, first_user.lname) 


@app.route("/api/setrooms", methods=['GET'])
def setrooms():
    try:
        r=0
        m=0
        f=0
        
        room = Rooms.query.all()
        child = Child.query.all()
        
        # for k in data:
        #     if k == 'title':
        #         event.title = data['title']

        for cap in room:
            r+=1
            if cap == "capacity":
                roomcap += cap[0]  

        x=0
        while x<=len(child):
            if child.gender == 'male': 
                m+=1
            elif child.gender =="female":
                f+=1
            x+=1
        #totalchildren = f+m
    
    except Exception as e:
        print(e)
        return make_response('Server error', 500)

@app.route("/api/auth/login", methods=['POST'])
def login():
    try:
        data = request.get_json()

        worker = Worker.query.filter_by(email=data['email']).first()

        if not worker:
            return make_response('Invalid credentials', 401)

        if check_password_hash(worker.password, data['password']):
            token = jwt.encode({'id': worker.public_id}, app.config['SECRET_KEY'])
            return jsonify({"token": token.decode('utf-8')})
        else:
            return make_response('Invalid credentials', 401)
    except Exception as e:
        print(e)
        return make_response('Server error', 500)

@app.route("/api/persons", methods=['GET'])
def get_all_persons():

    try:
        children = Child.query.all()
        workers = Worker.query.all()
        #parents = Parent.query.all()

#9832318 or 9433574 4921418

        output = []
        if request.get_json() == "childrenprofiles":
            for child in children:
                child_data = {
                    "id": child.cid,
                    "first_name" : child.fname,
                    "last_name" : child.lname,
                    "middle_name" : child.mname,
                    "date_of_birth" : child.dob,
                    "age" : child.age,
                    "parenthome" : child.parenthome,
                    "illness" : child.illness,
                    "mentor_comment" : child.mentor_comment,
                    "nurse_comment" : child.nurse_comment,
                    "phone" : child.phone,
                    "gender" : child.gender,
                    "parent" : child.parent,
                    "score" : child.score
                    }
                output.append(child_data)
                return jsonify({'children': output})

        if request.get_json() == "workerprofiles":
            for worker in workers:
                worker_data = {
                    "worker_email" : worker.worker_email,
                    "fname" : worker.fname,
                    "mname" : worker.mname,
                    "lname" : worker.lname,
                    "gender" : worker.gender,
                    "age" : worker.age,
                    "birth_of_date" : worker.dob,
                    "nurse" : worker.nurse,
                    "parent" : worker.parent
                    }
            output.append(worker_data)
            return jsonify({'workers': output})    
        

    except Exception as e:
        print(e)
        return make_response('Server error', 500)

@app.route("/api/createchild", methods=['POST'])
@token_required
def createchild(current_user):
    try:
        data = request.get_json()
        date = data['dob'].split("-")
        dofb = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
         
        child = Child(fname=data['fname'], mname=data['mname'], lname=data['lname'], phone=data['phone'],\
            dob=dofb, location = data['location'], gender=data['gender'], illness=data['illness'], age = data['age'],\
                parentemail = data['parentemail'])

        db.session.add(child)
        db.session.commit()
        return jsonify({"message":"Child Added"})

    except Exception as e:
        print(e)
        return make_response('Server error', 500)

@app.route("/api/createparent", methods=['POST'])
@token_required
def createparent(current_user):
    try:
        data = request.get_json()
        # date = data['dob'].split("-")
        # dofb = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
         
        parent = Parent(fname=data['fname'], lname=data['lname'], phone=data['phone'],\
           parent_email=data["parent_email"], gender=data['gender'])

        db.session.add(parent)
        db.session.commit()
        return jsonify({"message":"Parent Added"})
    
    except Exception as e:
        print(e)
        return make_response('Server error', 500)

@app.route("/api/createadult", methods=['POST'])
@token_required
def createadult(current_user):
    try:
        data = request.get_json()
        # date = data['dob'].split("-")
        # dob = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        
        if data["parent"] == True:
            parent = Parent(fname=data['fname'], lname=data['lname'], phone=data['phone'],\
            parent_email=data["email"], gender=data['gender'])
            db.session.add(parent)
            db.session.commit()
            return jsonify({"message":"Parent Added"})
        

        else:
            worker = Worker(worker_email = data["worker_email"], fname = data["fname"], mname =["mname"],\
                lname = data["lname"], age=data['age'],dob=data['dob'], gender = data["gender"], location = data["location"], nurse = data["nurse"])
            db.session.add(worker)
            db.session.commit()
            return jsonify({"message":"Worker Added"})
    
    except Exception as e:
        print(e)
        return make_response('Server error', 500)

@app.route("/api/Room/<room_id>", methods=["GET"])
def get_room(room_no):

    try:
        room = Rooms.query.filter_by(room_no=room_no)

        output = []
        for s in room:
            room_data = {
                "room_no": s.room_no,
                "gender": s.room_gender,
                "room_parent": s.room_parent,
                "room_score": s.room_score
            } 
            output.append(room_data)
        return jsonify({"room": output})

    except Exception as e:
        print(e)
        make_response('Server error', 500)

@app.route("/api/Rooms/<room_no>/scores", methods=['POST'])
def make_room(room_no):
    try:
        data = request.get_json()
        
        room = Rooms(room_no=data["room_no"], room_capacity=data["room_capacity"],\
            room_parent=data["room_parent"], room_children = data["room_children"], room_gender=data["room_gender"])

        db.session.add(room)
        db.session.commit()

        return jsonify({"message":"Room addeds"})

    except Exception as e:
        print(e)
        return make_response('Server error', 500)

def assign_rooms():
    girl = []
    girlsorted = []
    boy = []
    boysorted = []
    children = Child.query.all()
    event = Event.query.all()
    room = Room.query.all()
    count=0
    #organise registered children by gender
    for child in children:
        if child.gender == "male" and child.child_id in event.registered:
            boy += (child)
        elif child.sex()=="female" and child.child_id in event.registered:
            girl += (child)
    
    #mergesort children based on age
    

def mergeSort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    mergeSort(array, left_index, middle)
    mergeSort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)

  
def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

    print(array)
    

# @app.route("/api/addperson", methods=['POST'])
# @token_required
# def create_event(current_user):
#     try:
#         data = request.get_json()
#         date = data['start_date'].split("-")
#         start_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
#         date = data['end_date'].split("-")
#         end_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
#         event = Event(name=data['name'], description=data['description'], category=data['category'],\
#             title=data['title'], start_date=start_date, end_date=end_date,\
#                 venue=data['venue'], flyer=data['flyer'], creator=current_user.user_id)

#         db.session.add(event)
#         db.session.commit()
#         return jsonify({"message":"Event created"})
#     except Exception as e:
#         print(e)
#         return make_response('Server error', 500)
