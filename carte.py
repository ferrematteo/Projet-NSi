import folium 
import csv 


CarteNuage = folium.Map(location=[10, -60], zoom_start = 5)


latitude =[]
longitude =[]
nom =[]
pourcentage = []
pourcentageint=[]

with open ("zzdata.csv",newline="") as fichier :
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

for i in range(len(nom)):
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
CarteNuage.save("map.html")
