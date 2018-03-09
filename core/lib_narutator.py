import cv2
from PIL import Image, ImageFilter
import numpy as np
import os


def narutator(imagem):

    imagemColorida = imagem
    narutoFace = Image.open(os.path.join('static/img', 'naruto-uzumaki.png'))

    imagemDefault = np.asarray(imagemColorida).astype(np.uint8)
    cinza = cv2.cvtColor(imagemDefault, cv2.COLOR_RGB2GRAY)

    imgteste = Image.new('RGBA', narutoFace.size, (255, 255, 255, 255))

    # 1950x, 1000y
    cv2DetectFaces = cv2.CascadeClassifier(os.path.join('core', 'haarcascade_frontalface_default.xml'))
    facesEncontradas = cv2DetectFaces.detectMultiScale(cinza, 1.3, 5)

    for x, y, w, h in facesEncontradas:
        rosto = imagemDefault[y: y + h, x: x + w]

    PILrosto = Image.fromarray(rosto).convert('RGB').resize((1400, 1400))
    rosto_largura, rosto_altura = PILrosto.size
    offset = (int(1950-rosto_largura/2), int(1000-rosto_altura/2))
    imgteste.paste(PILrosto, offset)
    total = Image.alpha_composite(imgteste, narutoFace)
    return total

    # redimensionar altura 765 - 1680 = 915
    # redimensionar largura 1400 - 2440 = 1040

#narutator(Image.open('core/faustao.jpg')).show()
