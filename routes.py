
from application import app
from flask import render_template, flash,request,url_for,redirect
from application import db
from .forms import TodoForm
from datetime import datetime
from bson.objectid import ObjectId


@app.route("/")    # is used to define a route for the root URL ("/"). 
def get_todos():
    todos = []
    for todo in db.my_collection.find().sort("Date_Created", -1):  #gets data from collection and sorts
        todo["_id"] = str(todo["_id"])
        todo["Date_Created"] = todo["Date_Created"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)
    return render_template("view_todo.html",title = "LAYOUT PAGE",todos = todos)  #view_todo is HTML template which describes how the layout should be

@app.route("/add_todo",  methods = ['POST', 'GET'])
def add_todo():
    if request.method == "POST":  #if the form has been submitted,then the submitted form data is extracted and inserted into the database
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        todo_priority = form.priority.data
        completed = form.completed.data

        db.my_collection.insert_one({
            "Task" : todo_name,
            "Description" : todo_description,
            "Priority" : todo_priority,
            "Completed" : completed,
            "Date_Created" : datetime.utcnow()
        })
        flash("Task was successfully added", "Success")
        return redirect("/")
    else:  #an empty form is rendered for the user to fill out.

        form = TodoForm()
    return render_template("add_todo.html", form = form)
@app.route("/update_todo/<id>", methods = ['POST', 'GET'])
def update_todo(id):
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        todo_priority = form.priority.data
        completed = form.completed.data

        db.my_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "Task": todo_name,
            "Description": todo_description,
            "Priority" : todo_priority,
            "Completed": completed,
            "Date_Created": datetime.utcnow()
        }})
        flash("Task was updated successfully", "Success")
        return redirect("/")
    else:
        form = TodoForm()

        todo = db.my_collection.find_one({"_id": ObjectId(id)})
        form.name.data = todo.get("Task", None)
        form.description.data = todo.get("Description", None)
        form.priority.data = todo.get("Priority", None)
        form.completed.data = todo.get("Completed", None)

    return render_template("add_todo.html", form = form)
  
@app.route("/delete_todo/<id>")
def delete_todo(id):
    db.my_collection.find_one_and_delete({"_id": ObjectId(id)})
    flash("Task was deleted successfully", "Success")
    return redirect("/")