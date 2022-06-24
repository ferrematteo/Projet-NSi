""" L'objectif de se programme est de déterminer le pourcentage de pixel blanc sur une image,
 afin donc de déterminer le pourcentage de nuage présent sur une zone... 
 Pour que le résultat soit plus visible nous avons pour commencer transformé l'intégralité des pixels
 blanc en pixel vert... Et nous les avons ensuite comptés 

 A la fin, le programme divise le nombre de pixel blanc sur le nombre de pixel de l'image, en y enlevant les 
 pixels noirs qui représentent le contour de l'objectif de la caméra..

"""
import imageio
import matplotlib.pyplot as plt 
import numpy as np
import os 
import csv

nbpi= 5038848   # nb de pixel de l'image
nbpinoir = 2387839 #On a déterminé le nb de pixel noir dans une image afin d'enlever le contour


img = os.listdir()  # ouvre les images dans cette variable 


latitude = []
pourcentage=[]

def main():
    counter=0
    for a in img:
        counter+=1
        image = imageio.imread(a)
        plt.imshow(image)
        plt.show()
        
        masqueblanc= image[:,:,1]>=195
        image[masqueblanc]=[0,255,0]
        
        masquevert =image[:,:,1]==255

        pixelblanc= np.sum(image[:,:,1]==255)
        pourc= round((pixelblanc/(nbpi-nbpinoir))*100)  # le calcul du pourcentage 
        print("\nil y a ",pixelblanc,"pixel blanc")
        print("Le pourcentage de nuage sur l'image n°",counter,"est de",pourc,"%")
        print("La latitude de l'image n°",counter,"est :",latitude[counter])
        pourcentage.append(pourc)       #tout les pourcentages obtenus sont stockés dans une liste 

        plt.imshow(image)
        plt.show()
    
    
with open ("zzdata.csv",newline="") as fichier :
    ligne = csv.reader(fichier)
    for uneligne in ligne :
        latitude.append(uneligne[2])
        

