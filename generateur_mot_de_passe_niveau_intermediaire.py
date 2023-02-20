# Projet Python: Générateur de mots de passe sécurisés - niveau Intermediare

# Modules nécessaires
import string
import random

# Données
longueur = 10
lettres_minuscules = string.ascii_lowercase
lettres_majuscules = string.ascii_uppercase
nombres = string.digits
caracteres_speciaux = string.punctuation
mot_de_passe = '' 

# Manipulations des données
tous_les_caracteres = lettres_minuscules + lettres_majuscules + nombres + caracteres_speciaux

# Création de mots de passe
has_digit = False
has_lower = False
has_upper = False
has_special = False
found = False
while found != True:
  mot_de_passe = random.choices(tous_les_caracteres, k=longueur)
  for c in mot_de_passe:
    if c in lettres_minuscules: has_lower = True
    if c in lettres_majuscules: has_upper = True
    if c in nombres: has_digit = True
    if c in caracteres_speciaux: has_special = True
  found = all([has_lower, has_upper, has_digit, has_special])
  
  mot_de_passe = ''.join(mot_de_passe)
  print(mot_de_passe)
