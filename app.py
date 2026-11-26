from flask import Flask, render_template, request, redirect, session
from db import Base
import Models
import PyPDF2
import docx
import json

app = Flask(__name__)
app.secret_key = "secret001"

Base.metadata.create_all(bind=engine)

#HOME
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")
    
#SIGNUP
@app.route("/signup", methods=["GET" , "POST"])
def signup():
    db = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
if __name__ == "__main__":
    app.run(debug=True)