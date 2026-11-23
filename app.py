from flask import Flask, render_template, request, redirect, session
from db import Base
import Models

app = Flask(__name__)

@app.route("/")
def home():
    return "App is running!"

if __name__ == "__main__":
    app.run(debug=True)