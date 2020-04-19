from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db = SQLAlchemy(app)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/honey', methods=['GET', 'POST'])
def honey():
    return render_template('honey.html')


if __name__ == "__main__":
    app.run(debug=True)
