from flask import Flask, render_template, request, send_file
from PIL import Image
from io import BytesIO
from core import libanimate as anim

import numpy as np
import cv2
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/narutator', methods=['POST'])
def narutator():
    # # extract the image as string data
    # str_image = request.files.get('image-narutator').read()
    
    # # convert image FileStorage into an numpy array
    # np_image = np.fromstring(str_image, np.uint8)
    # img = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    img = Image.open(request.files.get('image-narutator').stream)
    # call narutator
    try:
        narutator_img = anim.narutator(img)
    except Exception as e:
        return str(e)
    
    # prepare image to be send by server
    str_io = BytesIO()
    narutator_img.save(str_io, 'PNG', quality=70)
    str_io.seek(0) 

    # send image back like a file 
    return send_file(str_io, mimetype='image/png')

@app.route('/lgenerator', methods=['POST'])
def lgenerator():

    img = Image.open(request.files.get('image-lgenerator').stream)
    # call lgenerator
    try:
        lgenerator_img = anim.lgenerate(img)
    except Exception as e:
        return str(e)
    
    # prepare image to be send by server
    str_io = BytesIO()
    lgenerator_img.save(str_io, 'PNG', quality=70)
    str_io.seek(0) 

    # send image back like a file 
    return send_file(str_io, mimetype='image/png')




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)