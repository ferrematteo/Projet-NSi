"""The goal of this program is to determine the percentage of white pixels in an image,
 in order to determine the percentage of clouds present in an area... 
 To make the result more visible, we have first transformed all the white pixels into green
 pixels... And then we counted them 

 At the end, the program divides the number of white pixels into the number of 
 pixels in the image, removing the black pixels that represent the outline of the image. 
"""

import imageio
import matplotlib.pyplot as plt 
import numpy as np
import os 
import csv

nbpi= 5038848 #number of pixels in the image
nbpinoir = 2387839 #number of black pixels


img = os.listdir()


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
        pourc= round((pixelblanc/(nbpi-nbpinoir))*100) # the calculation of the percentage 
        print("\nil y a ",pixelblanc,"pixel blanc")
        print("Le pourcentage de nuage sur l'image n°",counter,"est de",pourc,"%")
        print("La latitude de l'image n°",counter,"est :",latitude[counter])
        pourcentage.append(pourc) #All percentages obtained are stocked in a list 

        plt.imshow(image)
        plt.show()
    
    
with open ("zzdata.csv",newline="") as fichier :
    ligne = csv.reader(fichier)
    for uneligne in ligne :
        latitude.append(uneligne[2])
        

