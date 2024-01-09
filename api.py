#endpoint (Flash)
# ceci est un commentaire ?
from flask import Flask, jsonify, request, send_from_directory
from immo import liste_des_villes, liste_des_quartiers, quartiers_pour_ville,prix_pour_quartier_et_ville

app = Flask(__name__)

@app.route('/')
def serve_static_file():
    return send_from_directory('static', 'index.html')

@app.route('/villes', methods=['GET'])
def get_all_villes():
    all_villes = liste_des_villes()
    print("appel de la requête - /villes")
    return jsonify(all_villes)

@app.route('/quartiers', methods=['GET'])
def get_all_quartiers():
    all_quartiers = liste_des_quartiers()
    print("appel de la requête - /quartiers/all")
    return jsonify(all_quartiers)

@app.route('/quartiers/<string:ville>', methods=['GET'])
def get_quartiers(ville):
    quartiers = quartiers_pour_ville(ville)
    print("appel de la requête - /quartiers/<string:ville> - avec la ville",ville)
    return jsonify(quartiers)

@app.route('/prix/<string:ville>/<string:quartier>', methods=['GET'])
def get_prix(ville,quartier):
    prix= prix_pour_quartier_et_ville(ville,quartier)
    print("appel de la requête - /prix/<string:ville>/<string:quartier> - avec la ville",ville,"- avec le quartier",quartier)
    return jsonify(prix)

if __name__ == '__main__':
    app.run(debug=True)