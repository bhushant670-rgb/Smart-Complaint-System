from flask import Flask, request, render_template, redirect, url_for, session
from urllib.parse import urlparse
import mysql.connector as c
from dotenv import load_dotenv
import os
load_dotenv()
 
app=Flask(__name__)
app.secret_key="abc123"

def get_db_connection():
  url=os.getenv("MYSQL_PUBLIC_URL")
  parsed=urlparse(url)
  return c.connect(
   host=parsed.hostname,
   user=parsed.username,
   password=parsed.password,
   database=parsed.path[1:],
   port=parsed.port
  )

@app.route('/')
def home():
  return render_template('login.html')
  
@app.route('/login', methods=['POST'])
def login():
    email=request.form ["email"]
    password=request.form ["password"]
    session['users']=email
    if email == "admin@gmail.com" and password == "257":
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
  finally:
    con.close()

@app.route('/admin')
def admin():
  con= get_db_connection()
  cursor=con.cursor()
  cursor.execute("select * from complaint")
  data=cursor.fetchall()
  con.close()
  return render_template("admin.html",data=data)
 
if __name__=="__main__":
  app.run(debug=True)
 





     
