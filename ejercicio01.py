
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os


def op_multiplicacion(fileName, c):
	img = cv2.imread(fileName)
	img = img.astype(int)
	print (img.shape)
	h,w,canal = img.shape

	for i in range(canal):
		for j in range(img.shape[0]):
			for k in range(img.shape[1]):
				tmp =img[j][k][i] * c
				if (tmp >= 255 ):
				    img[j][k][i] = 255
				else:
				    img[j][k][i] = tmp
	imgResult = img
	cv2.imwrite('resultado_01_c_'+ str(c) +'.png',imgResult)


if __name__ == "__main__":

	op_multiplicacion('mul_4.jpg', 5)
	op_multiplicacion('mul_4.jpg', 7)
