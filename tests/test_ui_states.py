from fastapi.testclient import TestClient

from app.api.routes import create_app

client = TestClient(create_app())


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_status_requires_api_key():
    response = client.get('/api/status')
    assert response.status_code == 401


def test_chat_with_api_key():
    response = client.post('/api/chat', json={'message': 'Buenos días'}, headers={'X-API-Key': 'change-me'})
    assert response.status_code == 200
    assert 'response' in response.json()
