# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:18:18 2024

@author: Elisabeth
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def get_all_villes():
    return "bonjour"


if __name__ == '__main__':
    app.run(debug=True)