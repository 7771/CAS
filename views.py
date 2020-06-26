from flask import request, flash, jsonify, make_response, url_for, render_template
from app import db
import models
from models import * 
from forms import RegistrationForm, LoginForm

@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add-child', methods=['POST','GET'])
def add_child():
    child = Child(request.form['fname', request.form['lname']])
    if request.method == "POST":
        db.session.add(child)
        db.session.commit()    
        flash('New user was successfully added')        
        return redirect(url_for('show_children'))     
    
@app.route('/users')
def show_users():
    db = connect_db()
    cur = db.curser()
    cur.execute('select name, email from child order b id desc')
    users = cur.fetchall()
    return render_template('show_users.html', users = users)

#@app.route('/', methods=["GET"])
def capture():
    if request.method=='PUT':
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['dob']
        newPerson = Child(dob=dob, fname = fname, lname = lname)
        db.session.add(newPerson)
        db.session.commit()
    query = []
    for i in db.session.query(models.Child):
        query.append((i.dob, i.fname, i.lname))
        return i.dob, i.fname, i.lname

        #return redirect(url_for('newChild.html'))

"""
@app.route('/newPerson', methods=['GET','POST'])
def registerPerson():
    if request.method=='POST':
        dob = request.form['dob']
        fname = request.form['fname']
        lname = request.form['lname']
        mname = request.form['mname']
        parent = request.form['parent']
        illness = request.form['illness']
        phone = request.form['phone']
        newPerson = models.Child(dob=dob, fname = fname, lname = lname, mname=mname, parent=parent, illness=illness, phone=phone)
        db.session.add(newPerson)
        db.session.commit()
        return redirect(url_for('database'))
    else:
        return render_template('register.html', title='Register', form=form)

@app.route('/database', methods=['GET','POST'])
def database():
    query = []
    for i in session.query(models.Child):
        query.append((i.dob, i.fname, i.lname))
        return i.dob, i.fname, i.lname
   #return render_template('newRecord.html', query = query)

@app.route('/',methods=["GET"])
def search(column, table, text):
    ans =  table.query.filter_by(column=text)
    return ans

@app.route("/api/users/register", methods=["POST"])
def register():
    try:
        data = request.get_json()

        check = User.query.filter_by(email=data['email']).first()

        if not check:

            hashed_password = generate_password_hash(data['password'], method='sha256')
            public_id = str(uuid.uuid4())

            user = User(public_id=public_id, name=data['name'],\
                password=hashed_password, email=data['email'])
            db.session.add(user)
            db.session.commit()

            return jsonify({"message": "User successfully register"})
        else:
            return jsonify({"message": "User already exists or email is already taken"})

    except Exception as e:
        print(e)
        return make_response("Server error", 500)


# @app.route('/newParent')

# @app.route('/newWorker')

# @app.route('/DormAllocations')

# @app.route('/MyComments')

# @app.route('/Profile')

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Login', form=form)

@app.route('/dashboard', methods=['POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/createEvent', methods=['POST'])
def create_event():
    return render_template('eventForm.html')

@app.route('/viewEvent', methods=['POST'])
def view_event():
    return render_template('viewEvent.html')
"""
