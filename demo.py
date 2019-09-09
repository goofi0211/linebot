from flask import Flask 
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/login/')
def login():
    return 'login page'

if __name__ == '__main__':
    app.run()