from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:Ganugowda@789@localhost/student'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hepqfvfiipkrjb:dfac2829c80ced7c57095f2fcfca83746bb980b27ec4140d7f42a77e29c02d8c@ec2-18-207-95-219.compute-1.amazonaws.com:5432/d3lh2ikk5u2ho7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Student(db.Model):
	usn = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30))
	company = db.Column(db.String(30))
	designation = db.Column(db.String(30))
	package = db.Column(db.String(10))


@app.route('/')
def index():
	result = Student.query.all()
	return render_template('index.html',result=result)


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/process',methods = ['POST'])
def process():
    usn = request.form['usn']
    name = request.form['name']
    company = request.form['company']
    designation = request.form['designation']
    package = request.form['package']
    studentdata = Student(usn=usn,name=name,company=company,designation=designation,package=package)
    db.session.add(studentdata)
    db.session.commit()

    return redirect(url_for('index'))
