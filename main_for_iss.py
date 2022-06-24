# -*- coding: utf-8 -*-
"""
Le but de notre expérience est de détecter s'il y a plus de nuages au-dessus des mers ou des terres et de mesurer la probabilité de rencontrer des nuages au-dessus des mers ou au-dessus des terres.
Et aussi de voir s'il y a des variations en fonction de la latitude.

Dans la boucle principale on prend une image toutes les 30 secondes et on la nomme grâce à la variable photo_counter pour savoir dans quel ordre se trouvent les images.

L'expérience durera 176 minutes car nous prenons une marge d'erreur en cas de problème. 
Les propriétés de chaque image indiqueront la latitude et la longitude de l'iss, la date 
et l'heure seront dans un fichier exif et formatées dans une feuille de calcul appelée
data.csv.

"""

from pathlib import Path
from logzero import logger, logfile
from picamera import PiCamera
from orbit import ISS
from time import sleep
from datetime import datetime, timedelta
import csv

def create_csv_file(data_file):
    """A pour but de créer un fichier csv"""
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Counter", "Date/time", "Latitude", "Longitude")
        writer.writerow(header)

def add_csv_data(data_file, data):
    """Ajouter une ligne de données au fichier CSV data_file"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def convert(angle):
    """
    Convertissez un angle en une représentation
    appropriée (rationnelle)
    par exemple, 98° 34' 58.7 en "98/1,34/1,587/10".

    Retourne un tuple contenant un booléen et l'angle converti,
    le booléen indiquant si l'angle est négatif.
    """
    sign, degrees, minutes, seconds = angle.signed_dms()
    exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, exif_angle

def capture(camera, image):
    """Utilisez `camera` pour capturer un fichier `image` avec les données EXIF lat/long."""
    location = ISS.coordinates()

    # Convertir la latitude et la longitude en représentations EXIF appropriées.
    south, exif_latitude = convert(location.latitude)
    west, exif_longitude = convert(location.longitude)

    # Définir les balises EXIF spécifiant la localisation actuel.
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # Prendre l'image
    camera.capture(image)


base_folder = Path(__file__).parent.resolve()

# Definir un nom pour le fichier qui contient les 'log' 
logfile(base_folder/"events.log")

# Configure la caméra
cam = PiCamera()
cam.resolution = (2592, 1944) 

# Initialiser le fichier CSV
data_file = base_folder/"data.csv"
create_csv_file(data_file)

# Initialise le compteur de photo
counter = 1
# Enregistre l'heure de départ et l'heure actuelle
start_time = datetime.now()
now_time = datetime.now()
# Faire tourner une boucle pendant (presque) trois heures
while (now_time < start_time + timedelta(minutes=176)):
    try:
        location = ISS.coordinates()
        # Sauvegarder les données dans le fichier
        data = (
            counter,
            datetime.now(),
            location.latitude.degrees,
            location.longitude.degrees,
            
        )
        add_csv_data(data_file, data)
        # Capture image
        image_file = f"{base_folder}/photo_{counter:03d}.jpg"
        capture(cam, image_file)
        # Log 
        logger.info(f"iteration {counter}")
        counter += 1
        sleep(30)
        # Mettre à jour l'heure actuelle
        now_time = datetime.now()
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')
