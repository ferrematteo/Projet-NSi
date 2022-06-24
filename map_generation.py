""" L'objectif de ce programme est de créer une carte, dans laquelle toute
les images seront représentés par un point positionné à leurs position... 

Afin de déterminer la couverture nuageuse de plusieurs zones, nous avons créé un code couleur,
les images qui présentent une couverture nuageuse inférieur à 25% seront représentées par un point vert, 
celles dont la couverture nuageuse est comprise entre 25 et 50% seront représentées par des points jaune, 
et celle comprise entre 50 et 75% par des points orange. Enfin lorsque la couverture nuageuse sera supérieur 
à 75% les points seront rouge.

Cela nous permet d'avoir un résultat visuel de la couverture naugeuse en fonction de la localisation

"""

import folium 
import csv 


CarteNuage = folium.Map(location=[10, -60], zoom_start = 5)  #création de la carte 


latitude =[]
longitude =[]
nom =[]
pourcentage = []
pourcentageint=[]

with open ("zzdata.csv",newline="") as fichier :  # ouverture des fichiers .csv afin de récupérer les données relevés précédemment 
    ligne = csv.reader(fichier)
    for uneligne in ligne :
        latitude.append(uneligne[2])
        longitude.append(uneligne[3])
        nom.append(uneligne[0])

with open ("pourc.csv",newline="") as fichiera :
    lignea = csv.reader(fichiera)
    for unelignea in lignea :
        pourcentage.append(unelignea[0])
        


del(latitude[0])
del(longitude[0])
del(nom[0])

for i in pourcentage :
    pourcentageint.append(int(i))
    


for i in range(len(nom)):               #boucle qui place les points et qui met la couleur qui correspond à leurs couvertures nuageuses
    if pourcentageint[i] <= 25 :
        folium.Circle(
            [latitude[i], longitude[i]],
            radius=40000, fill_color ="green",color="green",fill_opacity=1).add_to(CarteNuage) 
            
    elif pourcentageint[i] <= 50 :
        folium.Circle(
            [latitude[i], longitude[i]],
            radius=40000, fill_color ="yellow",color="yellow",fill_opacity=1).add_to(CarteNuage) 
        
    elif pourcentageint[i] <= 75 :
        folium.Circle(
            [latitude[i], longitude[i]],
            radius=40000, fill_color ="orange",color="orange",fill_opacity=1).add_to(CarteNuage) 
        
    
    else :
        folium.Circle(
            [latitude[i], longitude[i]],
            radius=40000, fill_color ="red",color="red",fill_opacity=1).add_to(CarteNuage) 
       
        



CarteNuage                      
CarteNuage.save("map.html")         #création d'une page en HTML afin d'accéder à la carte
