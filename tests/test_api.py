import json
from app.main import app

def test_list_users():
    client = app.test_client()
    response = client.get('/users')
    assert response.status_code == 200

def test_create_user():
    client = app.test_client()
    payload = {"name": "Teste", "email": "teste@email.com"}
    response = client.post('/users', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 201
