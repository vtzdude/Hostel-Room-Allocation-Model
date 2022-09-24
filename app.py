from email.message import EmailMessage
import imp
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///record.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(200),nullable=False)
    Roll_Number=db.Column(db.Integer,nullable=False)
    Email=db.Column(db.String(200),nullable=False)
    Department=db.Column(db.String(200),nullable=False)
    Room_Number=db.Column(db.Integer,nullable=False)
def __repr__(self)->str:
    return f"{self.Serial_No} - {self.Name}"

    



@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        Name=request.form['Name']
        Email=request.form['Email']
        Roll_Number=request.form['Roll_Number']
        Department=request.form['Department']
        Room_Number=request.form['Room_Number']
        todo=Todo(Name=Name,Roll_Number=Roll_Number,Email=Email,Department=Department,Room_Number=Room_Number)
        db.session.add(todo)
        db.session.commit()
    allTodo=Todo.query.order_by(Todo.Room_Number).all()
    return render_template('index.html',allTodo=allTodo)

@app.route("/",methods=['GET','POST'])
def hello():
    if request.method=='POST':
        Name=request.form['Name']
        Email=request.form['Email']
        Roll_Number=request.form['Roll_Number']
        Department=request.form['Department']
        Room_Number=request.form['Room_Number']
        todo=Todo(Name=Name,Roll_Number=Roll_Number,Email=Email,Department=Department,Room_Number=Room_Number)
        db.session.add(todo)
        db.session.commit()
    allTodo=Todo.query.order_by(Todo.Room_Number).all()
    return render_template('index.html',allTodo=allTodo)

#@app.route('/show')
#def products():
#    allTodo = Todo.query.all()
#    print(allTodo)
#    return 'this is products page'
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        Name=request.form['Name']
        Email=request.form['Email']
        Roll_Number=request.form['Roll_Number']
        Department=request.form['Department']
        Room_Number=request.form['Room_Number']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.Name = Name
        todo.Email = Email
        todo.Roll_Number = Roll_Number
        todo.Department = Department
        todo.Room_Number = Room_Number
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)