import pytest
from api import liste_des_villes, liste_des_quartiers, quartiers_pour_ville, prix_pour_quartier_et_ville


def test_liste_des_villes():
    villes = liste_des_villes()
    assert len(villes) > 0
    assert isinstance(villes, list)

def test_liste_des_quartiers():
    quartiers = liste_des_quartiers()
    assert len(quartiers) > 0
    assert isinstance(quartiers, list)

def test_quartiers_pour_ville():
    quartiers = quartiers_pour_ville("Paris")
    assert len(quartiers) > 0
    assert isinstance(quartiers, list)
    
def test_prix_pour_quartier_et_ville():
    prix = prix_pour_quartier_et_ville("Paris","Est")
    assert len(prix) > 0
    assert isinstance(prix, str)
    
if __name__ == "__main__":
    pytest.main()