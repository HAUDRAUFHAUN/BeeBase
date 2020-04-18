from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/honey')
def honey():
    return render_template('honey.html')


if __name__ == "__main__":
    app.run(debug=True)
