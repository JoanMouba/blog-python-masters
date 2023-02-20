# Projet Python: Générateur de mots de passe sécurisés - débutants

# Modules nécessaires 
import random 

# Données
longueur = 10
lettres_minuscules = 'abcdefghijklmnopqrstuvwxyz' 
lettres_majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
nombres = '0123456789'
caracteres_speciaux = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"
mot_de_passe = ''

# Manipulations des données 
tous_les_caracteres = lettres_minuscules + lettres_majuscules + nombres + caracteres_speciaux

# Création de mots de passe et choisir
for i in range(5):
  mot_de_passe = random.choices(tous_les_caracteres, k=longueur)
  mot_de_passe = ''.join(mot_de_passe)
  print(mot_de_passe)
