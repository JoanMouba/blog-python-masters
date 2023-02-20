#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Projet Python: Générateur de mots de passe sécurisés - niveau Avance
# Ce code permet de générer des mots de passe sécurisés
# Important: Epignosis Center n'endosse aucune garantie que votre mot 
# de passe ne sera jamais craqué. Ni Epignosis Center, ni l'auteur,  
# ne peuvent être considéré responsables de quelque dommange que ce soit 
# suite à l'utilisation de ce code. Prenez vos responsabilités. 
# Bien que ce code soit utile, il est utilisé à but pédagogique ici. 
# 
# @uteur: Joan Mouba
# Epignosis Center 
# contact: epignosis.center@gmail.com 

import string
import secrets
import logging

logging.basicConfig(level=logging.DEBUG) 
# logging.disable()


class GenerateurDeMotsDePasse:
    """ Une classe pour la Génération de mot de passe """
    def __init__(self):
        self.longueur: int = int(input('Longueur de votre mot de passe? '))
        self._mot_de_passe: str = ''
        self._tous_les_caracteres: str = string.ascii_lowercase \
                                    + string.ascii_uppercase \
                                    + string.digits \
                                    + string.punctuation \

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self, valeur):
        if valeur < 8:
            logging.critical('longueur mininal du mot de passe doit être de 8')
            raise ValueError('Longueur minimale doit être 8')
        self._longueur = valeur

    def genere_un_mot_de_passe(self):
        """ Generene un mot de passe d'au moins 8 caractères et qui contient 
            au moins une minuscule, une majuscule, un chiffre et un caractère spécial
            Args: 
                pas d'Arguments
            Returns: 
                mot_de_passe: str
            Raises:
                ValueError: si la longueur du passe est inférieure à 8
        """
        
        all_conditions_met = False
      
        while all_conditions_met != True:
            has_digit: bool = False
            has_lower: bool = False
            has_upper: bool = False
            has_special: bool = False
            mot_de_passe = ''.join(secrets.choice(self._tous_les_caracteres) 
                                   for i in range(self._longueur)) 
            
            for c in mot_de_passe:
                if c.islower(): has_lower = True
                if c.isupper(): has_upper = True
                if c.isdigit(): has_digit = True
                if c in string.punctuation: has_special = True
                  
            all_conditions_met = all([has_lower, has_upper, has_digit, has_special])
            if all_conditions_met:
                mot_de_passe = ''.join(mot_de_passe)
                logging.info(mot_de_passe)
                return mot_de_passe

# Main function 
if __name__ == '__main__':
    generateur_alpha = GenerateurDeMotsDePasse()
    generateur_alpha.genere_un_mot_de_passe()
