# python-mongod-flask-web-App

Note Application Using Flask and MongoDB
Python is a very easy-to-learn language due to its user-friendly syntax. Moreover, Python has many open-source libraries, and almost every use case of Python has an existing library for that.
Python has several web application frameworks such as Django and Flask. Flask is an open-source, lightweight, Python web application framework.
Flask is designed to make it easy to get a simple application up and running.
We will use MongoDB as the database. MongoDB is a cross-platform, document-oriented database platform. It uses JSON objects as its data tuples.
When working with a web application, you might not know the exact data format being sent. In such cases, a NoSQL database such as MongoDB would be a good solution for data handling and storage.

Prerequisites
To follow along with this article, the following basic information will be essential:
•	Basic knowledge of working with Python.
•	Python installed on your computer.
•	MongoDB installed on your computer.
•	Pip installed on your computer.
Setting up the Flask application
In this section, you create a virtual environment in which Flask is installed. Using a virtual environment avoids installing Flask into a global Python environment and gives you exact control over the libraries used in an application. On your file system, create a project folder for this tutorial, such as hello_flask.

In that folder, use the following command (as appropriate to your computer) to create and activate a virtual environment named .venv based on your current interpreter:
# Windows
Pip install virtualenv
python -m venv .venv
.venv\scripts\activate
Open the project folder in VS Code by running code ., or by running VS Code and using the File > Open Folder command.
	In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:

1.	Open the project folder in VS Code by running code ., or by running VS Code and using the File > Open Folder command.
2.	In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the Python: Select Interpreter command:
 
3.	The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see Configuring Python environments). From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv:
 
4.	Run Terminal: Create New Terminal (Ctrl+Shift+`)) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.
Note: On Windows, if your default terminal type is PowerShell, you may see an error that it cannot run activate.ps1 because running scripts is disabled on the system. The error provides a link for information on how to allow scripts. Otherwise, use Terminal: Select Default Shell to set "Command Prompt" or "Git Bash" as your default instead.
5.	The selected environment appears on the right side of the VS Code status bar, and notice the ('.venv': venv) indicator that tells you that you're using a virtual environment:
 
6.	Install Flask in the virtual environment by running the following command in the VS Code Terminal:
7.	python -m pip install flask
Once activated, we need two dependencies:
•	flask - It is essential for setting up the web resource.
•	PyMongo - This will form the infrastructure from MongoDB to our application.
To install the dependencies, use the command below:
pip install Flask-PyMongo
Setting up MongoDB
To begin setting up MongoDB in our application, we need to create an app.py file at the project root folder. This will be our main file.
In this app.py file, add the following block of code:
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskProj"
mongo = PyMongo(app)

if __name__ == "__main__":
    app.run(debug=True)
Here, we have done basic configuration for a basic Flask app. We;
•	Have imported the necessary packages.
•	Set up the main app variable.
•	Initialized an instance of PyMongo.
•	Started the app in debug mode. This means that each change we make to the app will be reloaded automatically.
To test this, run the command below:
python -m flask run
The command above will start the application. You can access it from port number 5000; i.e. http://localhost:127.0.0.1:5000. For now, you will get a Not Found message since we have not defined any route.
