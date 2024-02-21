# Lit fichier, traite le fichier (Pandas)

import pandas as pd 
fichier = './data/prix_immobilier_fictif.csv'

def liste_des_villes():
    """ Retourne la liste de toutes les villes
    :return : liste de string"""
    
    df = pd.read_csv(fichier)
    
    #liste des villes sans doublons
    print("liste des villes :",df['Ville'].unique().tolist())
    return df['Ville'].unique().tolist()

def liste_des_quartiers():
    """ Retourne la liste de toutes les quartiers
    :return : liste de string"""
    
    df = pd.read_csv(fichier)
    
    #liste des quartier sans doublons
    print("liste des quartiers :",df['Quartier'].unique().tolist())
    return df['Quartier'].unique().tolist()

def quartiers_pour_ville(ville):
    """ Retourne la liste des quartiers pour une ville donnée
    :param ville: nom de la ville (string)
    :return : liste de string"""
    
    df = pd.read_csv(fichier)
    quartiers = df[df['Ville'] == ville]['Quartier'].unique().tolist()
    print("liste des quartiers de la ville",ville," :",quartiers)
    return quartiers

def prix_pour_quartier_et_ville(ville,quartier):
    """ Retourne le prix au m² d'un quartier donnée d'une ville donnée
    :param ville: nom de la ville (string), quartier : nom du quartier (string)
    :return : string"""
    
    df = pd.read_csv(fichier)
    
    prix = df[(df['Ville'] == ville) & (df['Quartier'] == quartier)]['Prix au m²']
    if not prix.empty:
        return 'Le quartier '+quartier+' de la ville '+ville+' possède un prix de '+str(prix.values[0])+' au mètres carrés'
    else:
        return "Prix non trouvé pour cette ville et ce quartier."

# liste_villes = liste_des_villes()
# liste_quartiers = liste_des_quartiers()
# quartier_Berlin=quartiers_pour_ville('Berlin')
# quartier_Londres=quartiers_pour_ville('Londres')