from PIL import Image, ImageFilter

import cv2
import numpy as np
import os

def generate(aimagem):
    hair = Image.open(os.path.join('static/img', 'L_hair.png')).convert('RGBA')
    # convertendo a imagem do tipo PIL para dois canais de cores
    imagem = aimagem.convert('L') 
    
    # convertendo imagem PIL para cv2
    cv2_imagem = np.asarray(imagem).astype(np.uint8)
    facial_cascade_dir = os.path.join('core', 'haarcascade_frontalface_default.xml')
    faces = cv2.CascadeClassifier(facial_cascade_dir).detectMultiScale(cv2_imagem, 1.3, 5)
    
    # adiciona o cabelo para cada posicao de face encontrada
    if len(faces) == 0:
        raise Exception('Nenhuma face encontrada')
    for x, y, w, h in faces:
        #hair = hair.resize((int(w*1.7), int(h*1.7)))
        hair = hair.resize((int(w+x - (w * 0.35)), int(h+y + (h * 0.5))))
        pX = x - int(w * 0.5)
        pY = y - int(h * 0.8)
        aimagem.paste(hair, (pX, pY), mask=hair)
        #a = cv2.rectangle(np.asarray(imagem).astype(np.uint8), (x, y), (x+w, y+h), (0, 255, 255), 2)
    return aimagem
