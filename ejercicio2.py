# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:08:17 2020

@author: MILAGROS PC
"""

import cv2
import os
import numpy as np

def pixel_division(folder, filename1, filename2):
    full_filename1 = os.path.join(folder, filename1)
    full_filename2 = os.path.join(folder, filename2)    
    img1 = cv2.imread(full_filename1,0)
    img2 = cv2.imread(full_filename2,0)
    img1 = img1.astype(int)
    img2 = img2.astype(int)
    
    imageOut = cv2.imread(full_filename1,0)
    imageOut = imageOut.astype(int)
    
    alto1, ancho1 = img1.shape
    alto2, ancho2 = img2.shape
    alto3, ancho3 = imageOut.shape

    
    c =100
    for x in range(alto1):
        for y in range(ancho1):
            imageOut[x][y] = int((img1[x][y] / img2[x][y])*c)
            
    
    # plt.imshow(imageOut)
                
   
    imaMin = np.min(imageOut)  # El menor valor de los pixeles
    imaMax = np.max(imageOut)  
    newMin = 0
    newMax = 255
        
    def escalar(pixel):
        return (pixel - imaMin)*((newMax - newMin)/(imaMax - imaMin) + newMin)
    
    
    for x in range(alto3):
        for y in range(ancho3):
            imageOut[x][y] = escalar(imageOut[x][y])
            
    
    salidaImg1 = "img/prueba_salida.png" # en vez de img pones static
    cv2.imwrite(salidaImg1,imageOut)
    img = cv2.imread('img/prueba_salida.png',0) # en vez de img pones static
    
    alto,ancho = img.shape
    
    result = img
    
    
    for x in range(alto):
        for y in range(ancho):
            if (10 < img[x][y] and img[x][y] < 170):
                result[x,y]=0
            else:
                result[x,y]=255
	    
                
    img_result = result  # importante
    full_filename_new = os.path.join(folder, 'sustraImg' + filename1)  # importante
    cv2.imwrite(full_filename_new, img_result)  # importante

    return full_filename_new  # importante



pixel_division('./img/','sub_1.jpg', 'sub_2.jpg')
    
