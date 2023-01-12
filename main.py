from flask import Flask
from fileReader import readFile

app = Flask(__name__)


@app.route('/')
def hello():
    return readFile('./index.html')