import cv2
from PIL import Image, ImageFilter
import numpy as np
import os

# todas as funcoes recebem e retornam uma variavel do tipo PIL.Image()
# diretorios de classificadores 
FACIAL_CASCADE_DIR = os.path.join('core', 'haarcascade_frontalface_default.xml')
EYE_CASCADE_DIR = os.path.join('core', 'haarcascade_eye.xml')

# classificadores 
faceClassifier = cv2.CascadeClassifier(FACIAL_CASCADE_DIR)  
eyeClassifier = cv2.CascadeClassifier(EYE_CASCADE_DIR)

# utilitarios lambda
classifierError = lambda(contours): len(contour) != 0


def lgenerate(aimagem):
    hair = Image.open(os.path.join('static/img', 'L_hair.png')).convert('RGBA')
    
    # convertendo a imagem do tipo PIL para dois canais de cores
    imagem = aimagem.convert('L') 
    
    # convertendo imagem PIL para cv2
    cv2_imagem = np.asarray(imagem).astype(np.uint8)
    facesEncontradas = faceClassifier.detectMultiScale(cv2_imagem, 1.3, 5)
    
    # adiciona o cabelo para cada posicao de face encontrada
    if classifierError(facesEncontradas):
        raise Exception('Nenhuma face encontrada')
    
    for x, y, w, h in facesEncontradas:
        #hair = hair.resize((int(w*1.7), int(h*1.7)))
        hair = hair.resize((int(w+x - (w * 0.35)), int(h+y + (h * 0.5))))
        pX = x - int(w * 0.5)
        pY = y - int(h * 0.8)
        aimagem.paste(hair, (pX, pY), mask=hair)
        #a = cv2.rectangle(np.asarray(imagem).astype(np.uint8), (x, y), (x+w, y+h), (0, 255, 255), 2)
    return aimagem

# convict conditiony
def narutator(imagem):
    narutoFace = Image.open(os.path.join('static/img', 'naruto-uzumaki.png'))
    
    imagemDefault = np.asarray(imagem).astype(np.uint8)
    cinza = cv2.cvtColor(imagemDefault, cv2.COLOR_RGB2GRAY)
    
    imgbg = Image.new('RGBA', narutoFace.size, (255, 255, 255, 255))
    # 1950x, 1000y
    facesEncontradas = cv2DetectFaces.detectMultiScale(cinza, 1.3, 5)
    
    if classifierError(facesEncontradas):
        raise Exception('Nenhuma face encontrada')

    for x, y, w, h in facesEncontradas:
        rosto = imagemDefault[y: y + h, x: x + w]    
    
    PILrosto = Image.fromarray(rosto).convert('RGB').resize((1400, 1400))
    rosto_largura, rosto_altura = PILrosto.size
    offset = (int(1950-rosto_largura/2), int(1000-rosto_altura/2))
    imgbg.paste(PILrosto, offset)
    total = Image.alpha_composite(imgbg, narutoFace)
    
    return total

# redimensionar altura 765 - 1680 = 915
# redimensionar largura 1400 - 2440 = 1040

