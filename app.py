from flask import Flask, request, render_template, redirect, url_for, session

import mysql.connector as c

app=Flask(__name__)
app.secret_key="abc123"

@app.route('/')
def home():
  return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email=request.form ["email"]
    password=request.form ["password"]
    session['users']=email
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
  con=c.connect(host="localhost",
                  user="root",
                  password="bhushan1234@*#",
                  database="college")
    
  cursor=con.cursor()
  query="""insert into complaint
          (name, room, hostel, floor, block, complaint, email)
          values (%s, %s, %s, %s, %s, %s, %s)"""

  values=(name, room, hostel, floor, block, complaint, email)

  try:
    cursor.execute(query,values)
    con.commit()
    return redirect(url_for('home'))
  except:
    return "Complaint already exists"

 
if __name__=="__main__":
  app.run(debug=True)





     
