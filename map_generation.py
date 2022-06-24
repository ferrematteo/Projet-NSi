"""The aim of this program is to create a map, in which all the
images will be represented by a point positioned at their location... 

In order to determine the cloud cover of several areas, we have created a colour code,
images with less than 25% cloud cover will be represented by a green dot, 
those with cloud cover between 25 and 50% will be represented by yellow dots, 
and those between 50 and 75% with orange dots. Finally, when the cloud cover is greater than 
75% the dots will be red.

This allows us to have a visual result of the cloud cover according to the location

"""







import folium 
import csv 


CarteNuage = folium.Map(location=[10, -60], zoom_start = 5) #creation of the map


latitude =[]
longitude =[]
nom =[]
pourcentage = []
pourcentageint=[]

with open ("zzdata.csv",newline="") as fichier : #opening of .csv files to retrieve previously collected data 
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
    

"""for i in range(len(nom)):
    folium.Marker([latitude[i], longitude[i]], popup=folium.Popup(nom[i]),
                 icon=folium.Icon(icon='flag')).add_to(CarteNuage)"""

for i in range(len(nom)):  #loop that places the points and sets the colour to match their cloud cover
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
CarteNuage.save("map.html")  #creation of an HTML page to access the map
