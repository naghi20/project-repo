# FastAPI example (or use Flask/Django)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Python app deployed via CI/CD!"}

# For Flask, replace with:
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def home(): return {"message": "Hello World!"}