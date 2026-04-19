 from flask import Flask, request, render_template, redirect, url_for, session

import mysql.connector as c
import os

app=Flask(__name__)
app.secret_key="abc123"

def get_db_connection():
  return c.connect(
    host=os.getenv("mysql.railway.internal"),
    user=os.getenv("root"),
    password=os.getenv("omEKbYmspiRMFdcTtHDzvxhfqWdIyQuZ"),
    database=os.getenv("railway"),
    port=int(os.getenv("3306"))
  )

@app.route('/')
def home():
  return render_template('login.html')
  
@app.route('/login', methods=['POST'])
def login():
    email=request.form ["email"]
    password=request.form ["password"]
    session['users']=email
    if email == "admin@gmail.com":
      return redirect(url_for('admin'))
    else:
      return redirect(url_for('complaint_page'))

@app.route('/complaint_page')
def complaint_page():
  return render_template('index.html')

@app.route('/complaint', methods=['POST'])
def complaint():
  if 'users' not in session:
    return redirect(url_for('home'))

  name=request.form ["name"]
  room=request.form ["room"]
  hostel=request.form ["hostel"]
  floor=request.form ["floor"]
  block=request.form ["block"]
  complaint=request.form ["complaint"]
  email=session['users']
  con=get_db_connection()
    
  cursor=con.cursor()
  query="""insert into complaint
          (name, room, hostel, floor, block, complaint, email, status)
          values (%s, %s, %s, %s, %s, %s, %s, %s)"""

  values=(name, room, hostel, floor, block, complaint, email, "pending")

  try:
    cursor.execute(query,values)
    con.commit()
    return redirect(url_for('home'))
  except:
    return "Error inserting data"

@app.route('/admin')
def admin():
  con= get_db_connection()
  cursor=con.cursor()
  cursor.execute("select * from complaint")
  data=cursor.fetchall()
  return render_template("admin.html",data=data)
 
if __name__=="__main__":
  app.run(debug=True)
 





     
