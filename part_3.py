import matplotlib.pyplot as plt
import os 
import numpy as np 
from array import *
import  part_1  as pr
import sys



def luminance(img):
    img = np.array(img)
    a = img.shape
    if img[1][1][1] == img [1][1][2] :
        s = 0 
        for i in range(a[0]):
            for j in range(a[1]):
                s = s + img[i][j][1]
        b = s / (a[0] * a[1])
    else :
        print("Cette image n'est pas au niveau gray ")
        sys.exit(1)
    return b




def contraste (img):
	img = np.array(img)
	a = img.shape
	d = luminance(img)
	if img[1][1][1] == img[1][1][2]:
		s = 0
		for i in range(a[0]):
			for j in range(a[1]):
				s = s + (img[i][j][1] - d) ** 2
		b = s /(a[1] * a[0])
	else : 
		print("Cette image n est pas au niveau gris")	
		sys.exit(1)
	return b
			


def profondeur (img) :
	img =np.array(img)
	a = img.shape
	Max = -255
	for i in range(a[0]) :
		for j in range (a[1]) :
			if Max < img[i][j][1] :
				Max = img[i][j][1]
	return Max	






















