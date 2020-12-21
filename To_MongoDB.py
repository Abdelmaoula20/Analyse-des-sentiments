# on va utiliser Mongoengine pour stocker les images
from PIL import Image
import json
from pymongo import MongoClient
import glob
## Créer la connexion et connecter à la base de données
from mongoengine import connect, Document,fields
from mongoengine.connection import disconnect
connect(db="test_kaisensData",host="192.168.99.100",port=27017)   # à remplacer ces parameters

##Crée une classe des utilsateurs

class User(Document):
    meta={"colection":"my_test"}
    username=fields.StringField(required=True)
    profile_image= fields.ImageField(thumbnail_size=(150,150,False))

## charger l'image
chirac = User(username='chirac')
my_image=open(path,'rb')
chirac.profile_image.replace(my_image, filename="Twitter_1.jpeg")
chirac.save()

## Récuperer l'image
user=User.objects(username="Abdelmaoula").first()
Image(user.profile_image.thumbnail.read())

# Stocker les textes

file_names = ['jacque chirac_Instagram.json', 'jacque chirac_Twitter.json']

for file_name in file_names:
    with open(file_name) as f:
        file_data = json.load(f)  # load data from JSON to dict
        for k, v in file_data.items():
            collection.insert_one(v)


disconnect()