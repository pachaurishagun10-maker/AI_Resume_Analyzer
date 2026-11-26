from flask import Flask, render_template, request, redirect, session
from db import Base
import Models
import PyPDF2
import docx
import json

app = Flask(__name__)
app.secret_key = "secret001"

Base.metadata.create_all(bind=engine)

@app.route("/")
def home():
    return "App is running!"

if __name__ == "__main__":
    app.run(debug=True)