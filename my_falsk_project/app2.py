from flask import Flask, render_template, request, redirect
from models import db
import os
from models import fcuser

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/register', Methods=['GET','POST'])
def registerUser():
    if request.method == GET:
        return render_template("join.html")
    else:
        userId = request.form.get('userId')
        userPassword = request.form.get('userPassword')
        userName = request.form.get('userName')
        print(userId)
        print(userPassword)
        print(usetName)
        return redirect('/')
    

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)