


import cv2
import numpy as np
from matplotlib import pyplot as plt


img1 = cv2.imread('sub_10.jpg', cv2.IMREAD_GRAYSCALE)

img2 = cv2.imread('sub_11.jpg', cv2.IMREAD_GRAYSCALE)

img1 = img1.astype(int)
img2 = img2.astype(int)



img2.shape = img1.shape #Adecuamos los tamaños de Ambos archivos para que sean iguales

alto1,ancho1 = img1.shape
#alto2,ancho2 = img2.shape


for i in range(alto1):
    for j in range(ancho1):
        img = abs((img2[i][j]/img1[i][j]))*30
        
        if (img == 0):
            img1[i][j] = 0
        else:
            img1[i][j] = img
        
##############Contrast######################
salidaImg1 = "prueba_salida2.png" # en ez de img pones static
cv2.imwrite(salidaImg1,img1)
img = cv2.imread('prueba_salida2.png',0) # en ez de img pones static

a = 0  # límite inferior
b = 255  # límite superior
c = np.min(img)  # El menor valor de los pixeles
d = np.max(img)  # El mayor valor de los pixeles

alto, ancho = img.shape 

result = img

def point_operator(pixel_RGB):
    return (pixel_RGB - c) * ((b - a) / (d - c) + a)

for x in range(alto):
    for y in range(ancho):
        result[x][y] = point_operator(img[x][y])

img_result = result  # importante
#full_filename_new = os.path.join(folder, 'ResultCambio' + filename1)  # importante
#cv2.imwrite(full_filename_new, img_result)  # importante

#return full_filename_new  # importante

cv2.imshow('Resultado',img_result)
cv2.imwrite('resultado_3.png',img_result)
