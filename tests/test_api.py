import pytest
from app.main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_list_users(client):
    response = client.get('/users')
    assert response.status_code == 200

def test_create_user(client):
    response = client.post('/users', json={"name": "Test User", "email": "test@example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data
