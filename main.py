from flask import render_template
from flask import Flask, jsonify, redirect
from task import random_word

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    words = random_word()
    return render_template('index.html', en_word=words.english_word, ru_word=words.russian_word)

@app.route('/')
def main():
    return render_template("index.html", en_word="Hello", ru_word="Привет")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)