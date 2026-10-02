from django.shortcuts import render, redirect
import os
import mysql.connector

def insertdata(name,mail,gen,dob,password):
    
    conn = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database="potatodb"
    )

    cursor = conn.cursor()

    try:
        sql = """INSERT INTO signup(name, mail, gen, dob, password) VALUES (%s, %s, %s, %s, %s)"""

        values = (name,mail,gen,dob,password)

        cursor.execute(sql, values)

        conn.commit()

        print(cursor.rowcount, "Record Inserted")

        cursor.close()
        conn.close()

        return True
    
    except Exception as e:
        return e

   
    


def signup(request):

    name = request.POST.get("name")
    mail = request.POST.get("email")
    gen = request.POST.get("gender")
    dob = request.POST.get("dob")
    password = request.POST.get("password")

    if name!=None and mail != None and gen !=None and dob !=None and password != None:
        print(name)
        x = insertdata(name,mail,gen,dob,password)
        print('insert: ',x)

    return render(request, 'signup.html')

def signin(request):

    mail = request.POST.get('email')
    pas = request.POST.get('password')

    if mail != None and pas != None:

        try:
            conn = mysql.connector.connect(
                host=os.environ.get("DB_HOST"),
                user=os.environ.get("DB_USER"),
                password=os.environ.get("DB_PASSWORD"),
                database="potatodb"
            )

            cursor = conn.cursor()

            cursor.execute("SELECT password FROM signup WHERE email=%s", (mail,))
            row = cursor.fetchone()

            cursor.close()
            conn.close()

            if row and row[0] == pas:
                return redirect('home')

        except Exception as e:
            print(e)

    return render(request, 'signin.html')

def land(request):

    return render(request,'landing.html')