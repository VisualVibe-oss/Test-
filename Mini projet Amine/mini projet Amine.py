from random import *
import matplotlib.pyplot as plt
from numpy import *


def afficher(img):
    plt.axis("off")
    plt.imshow(img,vmin=0,cmap="gray")
    plt.show()
def ouvrirImage(chemin):
    img=plt.imread(chemin)
    return img
def saveImage(img):
    plt.imsave("image1.png",img)
#######################
################################################PARTIE 2 22 22 2 2 2 2 2 2 ##################################
def image_noire(h,l):
    T=zeros([h,l],dtype=int)
    return T
def imageblanche(h,l):
    T=ones([h,l],dtype=int)
    return T
def creerImgBlancNoir(h,l):
    T=[[0]*l for i in range(h)]
    for i in range(h):
        for j in range(l):
            T[i][j]=(i+j)%2
    return T
def negative(img):
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j]==1:
                img[i][j]=0
            else:
                img[i][j]=1
    return img

######################################PARTI 3 3 3 3 3 3 3 3 3 3 3   3 3 3 3 3 3 PARTI######################################

def luminance(img):
    s=0
    for i in range(len(img)):
        for j in range(len(img[0])):
            s=s+img[i][j]
    return s/len(img)*len(img[0])
def contrast(img):
    s=0
    N=len(img)*len(img[0])
    for i in range(len(img)):
        for j in range(len(img[0])):
            m=luminance(img)
            s=s+(1/N)*(img[i][j]-m)**2
    return s
def profondeur(img):
    max=-255
    for i in range(len(img)):
        for j in range(len(img[0])):
            if img[i][j]>max:
                max=img[i][j]
    return max
###############################PARTIE 44444 4 4 4 4 4 4 4 4  4 4 4 4 4 44 4 #############################
def inverser(img):
    l=len(img[0])
    h=len(img)
    iv=[[0]*l for i in range(h)]
    for i in range(h):
        for j in range(l):
            iv[i][j]=255-img[i][j]
    return iv
def flipH(img):
    l = len(img[0])
    h = len(img)
    fp=[[0]*l for i in range(h)]
    for i in range(h):
        for j in range(l):
            fp[i][j]=img[i][l-1-j]
    return fp
def poserV(img1,img2):
    l = len(img1[0])
    h = len(img1)
    ps=[[0]*2*l for i in range(h)]#initialisation d'une Matrice par la meme hauteur mais par une longueur de 2*l
    for i in range(h):
        for j in range(l):
            ps[i][j]=img1[i][j]
    for i in range(h):
        for j in range(l):
            ps[i][j+l]=img2[i][j]
    return ps
def poserH(img1,img2):
    l = len(img1[0])
    h = len(img1)
    ps=[[0]*l for i in range(h*2)]#initialisation d'une Matrice par la meme longueur mais par une hauteur de 2*h
    for i in range(h):
        for j in range(l):
            ps[i][j]=img1[i][j]
            ps[i+h][j]=img2[i][j]
    return ps
##############################################PARIE 555 5 5 5 5 5 5 5 5 5########################################
def initImageRGB(c,l):
    img=[[[randrange(255) for k in range(3)] for i in range(c)] for j in range(l)]# c indique le nombre de colone et l indique le nombre de ligne
    return img
def symetrieH(img):#fonction return une image symétrie par rapport a horizontal
    img_inv=initImageRGB(len(img[0]),len(img))
    for i in range(len(img)):
        for j in range(len(img[0])):
            img_inv[i][j]=img[len(img)-1-i][j]
    return img_inv
def symetrieV(img):
    img_inv=initImageRGB(len(img[0]), len(img))
    for i in range(len(img)):
        for j in range(len(img[0])):
            img_inv[i][j] = img[i][-j-1+len(img[0])]
    return img_inv
def Moyenne(L): #fonction return la moyenne d'une List de trois couche
    s=0
    for i in range(3):
        s=s+L[i]
    return s//3
def  grayscale(img):
    L=[[0]*len(img[0]) for i in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[0])):
            L[i][j]=Moyenne(img[i][j])#utilisation de la fonction Moyenne pour obtenir une image gray
    return L
if __name__ == "__main__":
    c=1
    while (c == 1 or c == 2 or c == 3 or c == 4 or c == 5):
         print("*****************************ENTRER QUELLE PARTIE VOUS VOULEZ ACEDER***********************")
         print("1-Partie 1");print("2-Partie 2");print("3-Partie 3");print("4-Partie 4");print("5-Partie 5")
         c = int(input("entrer le numero de Partie:"))

         match c:
            case 1:
                print("1-AfficherImg")
                print("2-saveImage")
                f = int(input("entrer la fonction :"))
                match f:#la fct macth joue le role du fct switch
                    case 1:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        afficher(img)
                    case 2:
                        ch = str(input("entrer le chemin de l'image"))
                        img = ouvrirImage(ch)
                        saveImage(img)
            case 2:
                print("1-image_noire")
                print("2- image_blanche")
                print("3-creerImgBlancNoir")
                print("4- negatif")
                f = int(input("entrer la fonction :"))
                match f:
                    case 1:
                        L = int(input("Hauteur:"))
                        l = int(input("largeur:"))
                        img = image_noire(L, l)
                        afficher(img)
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips=='o':# si ips='o' l'image va etre sauvegarder par la fct saveImage sous le nom de image1
                            saveImage(img)
                    case 2:
                        L = int(input("Hauteur:"))
                        l = int(input("largeur:"))
                        img = imageblanche(L, l)
                        afficher(img)
                        ips = input("voulez vous sauvegrader cette image o/n:")
                        if ips == 'o':
                            saveImage(img)
                    case 3:
                        L = int(input("Hauteur:"))
                        l = int(input("largeur:"))
                        img = creerImgBlancNoir(L, l)
                        afficher(img)
                        ips = input("voulez vous sauvegrader cette image o/n:")
                        if ips == 'o':
                            saveImage(img)
                    case 4:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        afficher(negative(img))
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips=='o':
                            saveImage(negative(img))
            case 3:
                print("1-Luminance")
                print("2- contrast")
                print("3-profondeur")
                f = int(input("entrer la fonction :"))
                match f:
                    case 1:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        print(luminance(img))
                    case 2:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        print(contrast(img))
                    case 3:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        print(profondeur(img))
            case 4:
                print("1-inverser")
                print("2-flipH")
                print("3-poserV")
                print("4- poserH")
                f = int(input("entrer la fonction :"))
                match f:
                    case 1:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        afficher(inverser(img))
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips=='o':
                            saveImage(inverser(img))
                    case 2:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        afficher(flipH(img))
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips=='o':
                            saveImage(flipH(img))
                    case 3:
                        ch1 = input("entrer le chemin de l'image 1")
                        ch2 = input("entrer le chemin de l'image 2")
                        img1 = ouvrirImage(ch1)
                        img2 = ouvrirImage(ch2)
                        afficher(poserV(img1, img2))
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips=='o':
                            saveImage(poserV(img1,img2))

                    case 4:
                        ch1 = input("entrer le chemin de l'image 1")
                        ch2 = input("entrer le chemin de l'image 2")
                        img1 = ouvrirImage(ch1)
                        img2 = ouvrirImage(ch2)
                        afficher(poserH(img1, img2))
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips=='o':
                            saveImage(poserH(img1,img2))
            case 5:
                print("1-initImageRGB")
                print("2-symetrieH")
                print("3-symetrieV")
                print("4- grayscale")
                f = int(input("entrer la fonction :"))
                match f:
                    case 1:
                        L = int(input("Hauteur:"))
                        l = int(input("largeur:"))
                        img = initImageRGB(l, L)
                        afficher(img)
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips=='o':
                            saveImage(img)
                    case 2:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        afficher(symetrieH(img))
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips=='o':
                            saveImage(symetrieH(img))
                    case 3:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        afficher(symetrieV(img))
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips==o:
                            saveImage(symetrieV(img))
                    case 4:
                        ch = input("entrer le chemin de l'image")
                        img = ouvrirImage(ch)
                        img2 = grayscale(img)
                        afficher(img2)
                        ips=input("voulez vous sauvegrader cette image o/n:")
                        if ips=='o':
                            saveImage(img2)





















































