from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home2.html')

app.run()