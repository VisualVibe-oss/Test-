import matplotlib.pyplot as plt
import part_1 as pr
import os
import numpy as np

def flip(img):
    img = np.array(img)
    a = img.shape
    inverted_rows = []  # Créer une liste pour stocker les lignes inversées
    
    for i in range(a[0]):
        b = []
        for j in range(a[1]):
            b.append(img[i][j][1])
        b.reverse()
        inverted_rows.append(b)  # Ajouter la ligne inversée à la liste
        
    c = np.array(inverted_rows)  # Convertir la liste en tableau NumPy
    
    return c






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



path = r"C:\Users\pc\OneDrive\Desktop\python\project\lena512.gif"
img = pr.open_image (path)
c = flip(img)
plt.imshow(c)
plt.show()
