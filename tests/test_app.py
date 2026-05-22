import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

import pytest
from app import app, init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DATABASE'] = ':memory:'
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

def test_index(client):
    res = client.get('/')
    assert res.status_code == 200

def test_add_task(client):
    res = client.post('/add', data={'title': 'Test Task'}, follow_redirects=True)
    assert res.status_code == 200