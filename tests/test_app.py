import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Dark Roast Coffee House' in response.data
    assert b'Where Every Cup Tells a Story' in response.data

def test_menu_page(client):
    """Test the menu page loads successfully."""
    response = client.get('/menu')
    assert response.status_code == 200
    assert b'Dark Roast Coffee House' in response.data

def test_about_page(client):
    """Test the about page loads successfully."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About Our Coffee House' in response.data

def test_contact_page(client):
    """Test the contact page loads successfully."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Get In Touch' in response.data

def test_404_page(client):
    """Test 404 error handling."""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404

def test_home_contains_signature_blends(client):
    """Test that home page contains signature blends section."""
    response = client.get('/')
    assert b'Our Signature Blends' in response.data
    assert b'Midnight Espresso' in response.data
    assert b'Velvet Latte' in response.data

def test_home_contains_gallery(client):
    """Test that home page contains image gallery."""
    response = client.get('/')
    assert b'Our Craft' in response.data
    assert b'gallery' in response.data

def test_home_contains_prices(client):
    """Test that home page displays prices."""
    response = client.get('/')
    assert b'$4.50' in response.data
    assert b'$5.25' in response.data
    assert b'$4.75' in response.data

def test_content_type(client):
    """Test that response content type is HTML."""
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'






