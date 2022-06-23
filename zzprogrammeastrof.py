import imageio
import matplotlib.pyplot as plt 
import numpy as np
import os 
import csv

nbpi= 5038848
nbpinoir = 2387839 #On a déterminé le nb de pixel noir dans une image afin d'enlever le contour


img = os.listdir()
del img[-1]
del img[-1]
del img[-1]
del img[-1]
del img[-1]
del img[-1]
del img[-1]
del img[-1]

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
        pourc= round((pixelblanc/(nbpi-nbpinoir))*100)
        print("\nil y a ",pixelblanc,"pixel blanc")
        print("Le pourcentage de nuage sur l'image n°",counter,"est de",pourc,"%")
        print("La latitude de l'image n°",counter,"est :",latitude[counter])
        pourcentage.append(pourc)

        plt.imshow(image)
        plt.show()
    
    
with open ("zzdata.csv",newline="") as fichier :
    ligne = csv.reader(fichier)
    for uneligne in ligne :
        latitude.append(uneligne[2])
        

