import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test the homepage renders correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Enter your name' in response.data

def test_welcome_message(client):
    """Test the welcome message is shown when a name is submitted"""
    response = client.post('/', data={'username': 'Darshan'})
    assert response.status_code == 200
    assert b'Welcome, Darshan!' in response.data
