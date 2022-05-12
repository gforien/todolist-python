import socket
from http import HTTPStatus
from flask import Flask

app = Flask(__name__)

@app.get("/")
def get_root():
    return "todolist-service-python", HTTPStatus.OK

@app.get("/status")
def get_status():
    return "OK", HTTPStatus.OK

@app.get("/pod")
def get_pod():
    pod_name = socket.gethostname()
    return pod_name, HTTPStatus.OK
