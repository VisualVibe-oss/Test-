from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

"""
path = input("Entrer le nom de l image :\n\n")
os.system("cls")

"""


def open_image(path):
    try:
        img = plt.imread(path)
        return img
    except FileNotFoundError:
        print("L'image  n'existe pas")
        sys.exit(1)


def Afficher_image(img):
    plt.axis("off")
    plt.imshow(img, cmap="gray")
    plt.show()


def save_image(img, path):
    le_nom_image = os.path.basename(
        path
    )  # renvoit le nom image qui se trouve en "path"
    p = int(
        input(
            "Appuier sur 1 pour si tu veut changer le nom d image et leur extension et 0 pour le consever : \n\n"
        )
    )
    if p == 1 or p == 0:
        if p == 0:
            plt.imsave(le_nom_image, img)
        else:
            nouveau_N = input("Entrer le nouveau nom et le nouveau extension :\n\n")
            plt.imsave(nouveau_N, img)
    else:
        sys.exit(0)


path = r"C:\Users\pc\OneDrive\Desktop\3azi.jpeg"
open_image(path)
