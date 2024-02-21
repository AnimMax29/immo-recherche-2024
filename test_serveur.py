import pytest
from flask import Flask

from api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_all_villes(client):
    response = client.get('/villes')
    assert response.status_code == 200
    assert b"villes" in response.data

def test_get_all_quartiers(client):
    response = client.get('/quartier/all')
    assert response.status_code == 200
    assert b"quartier" in response.data

def test_get_quartiers(client):
    response = client.get('/quartiers/Paris')
    assert response.status_code == 200
    assert b'quartiers' in response.data

def test_get_prix(client):
    response = client.get('/quartiers/Paris/Est')
    assert response.status_code == 200
    assert b"Paris" in response.data
    assert b"Est" in response.data