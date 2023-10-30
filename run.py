from flask import Flask, jsonify, make_response
from http import HTTPStatus
from src.app import create_app

app = create_app()

@app.route("/welcome", methods=["GET"]) #@app.get("/welcome")
def welcome():
    return "Ciao"

@app.route("/", methods=["GET"]) #@app.get("/welcome")
def ciao():
    return [
        {"message" : "Ciao"}, {"message" : "Buongiorno"}, HTTPStatus.CREATED
    ]

