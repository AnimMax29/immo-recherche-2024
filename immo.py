# Lit fichier, traite le fichier (Pandas)

import pandas as pd 

def liste_des_villes():
    """ Retourne la liste de toutes les villes
    :return : liste de string"""
    
    df = pd.read_csv('./data/prix_immobilier_fictif.csv')
    
    #liste des villes sans doublons
    return df['Ville'].unique().tolist()