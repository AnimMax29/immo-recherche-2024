# Lit fichier, traite le fichier (Pandas)

import pandas as pd 

def liste_des_villes():
    """ Retourne la liste de toutes les villes
    :return : liste de string"""
    
    df = pd.read_csv('./data/prix_immobilier_fictif.csv')
    
    #liste des villes sans doublons
    print("liste des villes :",df['Ville'].unique().tolist())
    return df['Ville'].unique().tolist()

def liste_des_quartiers():
    """ Retourne la liste de toutes les quartiers
    :return : liste de string"""
    
    df = pd.read_csv('./data/prix_immobilier_fictif.csv')
    
    #liste des quartier sans doublons
    print("liste des quartiers :",df['Quartier'].unique().tolist())
    return df['Quartier'].unique().tolist()

def quartiers_pour_ville(ville):
    """ Retourne la liste des quartiers pour une ville donnée
    :param ville: nom de la ville (string)
    :return : liste de string"""
    
    df = pd.read_csv('./data/prix_immobilier_fictif.csv')
    quartiers = df[df['Ville'] == ville]['Quartier'].unique().tolist()
    print("liste des quartiers de la ville",ville," :",quartiers)
    return quartiers

# liste_villes = liste_des_villes()
# liste_quartiers = liste_des_quartiers()
# quartier_Berlin=quartiers_pour_ville('Berlin')
# quartier_Londres=quartiers_pour_ville('Londres')