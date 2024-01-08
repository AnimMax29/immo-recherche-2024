#endpoint (Flash)
# ceci est un commentaire ?
from flask import Flask, jsonify, request
from immo import liste_des_villes, liste_des_quartiers, quartiers_pour_ville

app = Flask(__name__)

@app.route('/villes', methods=['GET'])
def get_all_villes():
    all_villes = liste_des_villes()
    print("appel de la requête - /villes")
    return jsonify(all_villes)

@app.route('/quartier/all', methods=['GET'])
def get_all_quartiers():
    all_quartiers = liste_des_quartiers()
    print("appel de la requête - /quartiers/all")
    return jsonify(all_quartiers)

@app.route('/quartiers/<string:ville>', methods=['GET'])
def get_quartiers(ville):
    quartiers = quartiers_pour_ville(ville)
    print("appel de la requête - /quartiers/<string:ville> - avec la ville",ville)
    return jsonify(quartiers)

if __name__ == '__main__':
    app.run(debug=True)