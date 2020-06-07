import cv2
import os
import numpy as np
from matplotlib import pyplot as plt 
import math

def ope_blend(folder, filename1, filename2, x):
    full_filename1 = os.path.join(folder, filename1)
    full_filename2 = os.path.join(folder, filename2)    
    img1 = cv2.imread(full_filename1)
    img2 = cv2.imread(full_filename2) 

    # ajustamos el tamaño de la imagen 2 a la de la imagen 1
    img2 = cv2.resize((img2), (img1.shape[1], img1.shape[0]))

    #creamos una imagen en negro
    out = np.zeros(shape=img1.shape,dtype=np.uint8)

    for i in range(len(img1[0][0])):
        for j in range(img1.shape[0]):
            for k in range(img1.shape[1]):
                out[j][k][i] = x*img1[j][k][i] + (1-x)*img2[j][k][i]
        
    img_result = out  # importante
    full_filename_new = os.path.join(folder, 'blendHero09' + filename1)  # importante
    cv2.imwrite(full_filename_new, img_result)  # importante

    return full_filename_new  # importante
        
  

#ope_blend('img/','add_10.jpg','add_11.jpg', 0.1)
# ope_blend('img/','endgame.jpg','viuda.jpg',0.25) 
# ope_blend('img/','endgame.jpg','viuda.jpg',0.5) 
ope_blend('img/','endgame.jpg','viuda.jpg',0.9) 