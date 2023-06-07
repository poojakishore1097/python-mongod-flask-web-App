from flask import Flask, render_template, request, session, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId
from datetime import datetime
import bson
import uuid #for generating unique task id

app = Flask(__name__)

app.config["MONGO_URI"]="mongodb://localhost:27017/flaskproject"
app.secret_key = 'abc'
mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        users = mongo.db.Users.find({'username': session['username']})
        return render_template('pages/login.html', users=users)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.Users
        login_user = users.find_one({'username': request.form['username']})
        if login_user:
            if request.form['password'] == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('home'))
        error = 'Invalid username or password'
        return render_template('pages/login.html', error=error)
    return render_template('pages/login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = mongo.db.Users
        existing_user = users.find_one({'username': request.form['username']})
        if existing_user is None:
            users.insert_one({
                'username': request.form['username'],
                'password': request.form['password'],
                'email': request.form['email']
            })
            return redirect(url_for('login'))
        error = 'user with the email already exists'
        return render_template('pages/signup.html', error=error)
    return render_template('pages/signup.html')

@app.route("/home")
def home():
    search_query = request.args.get('search')
    if search_query:
        tasks = mongo.db.Tasks.find({'$or': [
            {'task_name': {'$regex': search_query, '$options': 'i'}},
            {'description': {'$regex': search_query, '$options': 'i'}},
            {'status': {'$regex': search_query, '$options': 'i'}}
        ]}).sort("date",-1)
    else:
        tasks = mongo.db.Tasks.find()
    return render_template("pages/home.html", homeIsActive=True,addNoteIsActive=True,tasks=tasks,search_query=search_query)


@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        description = request.form['description']
        status = request.form['status']
        assigned_user = request.form['assigned_user']

        # Get the current date and time
        date = datetime.now()
        
        assigned_user = mongo.db.Users.find_one({'email': assigned_user})

        if assigned_user is None:
            return 'Assigned user not found. Please check the username and try again.'

         # Generate a unique task ID
        #task_id = str(uuid.uuid4())
        if assigned_user:
            task = {
                # '_id': task_id,
                'task_name': task_name,
                'description': description,
                'status': status,
                'date': date,
                'assigned_user': assigned_user
            }
            mongo.db.Tasks.insert_one(task)
            # Send email to assigned user here
            # ...
            return redirect(url_for('home'))
        else:
            return 'Assigned user not found'

    users = mongo.db.Users.find()
    return render_template('pages/add_task.html', users=users)



    
@app.route('/edit_task', methods=['GET','POST'])
def editNote():

    if request.method == "GET":

        # get the id of the note to edit
        taskId = request.args.get('form')


        # get the note details from the db
        tasks = dict(mongo.db.Tasks.find_one({"_id":ObjectId(taskId)}))

        # direct to edit note page
        users = mongo.db.Users.find()
        return render_template('pages/edit_task.html',tasks=tasks,users=users)

    elif request.method == "POST":

        #get the data of the note
       taskId = request.form['_id']
       task_name = request.form['task_name']
       description = request.form['description']
       status = request.form['status']  
       assigned_user = request.form['assigned_user']
        
        # update the data in the db
       mongo.db.Tasks.update_one({"_id":ObjectId(taskId)},
                              {"$set":{"task_name":task_name,
                                       "description":description,
                                       "status":status,
                                       "assigned_user":assigned_user
                            }})  

        # redirect to home page
    return redirect(url_for('home'))  


@app.route('/delete_task', methods=['POST'])
def deleteNote():
    taskId = request.form['_id']
    mongo.db.Tasks.delete_one({ "_id": ObjectId(taskId)})
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
