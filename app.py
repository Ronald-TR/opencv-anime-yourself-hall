from flask import Flask, render_template
import core.lib_narutator

import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/narutator')
def narutator():
    return ''



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)