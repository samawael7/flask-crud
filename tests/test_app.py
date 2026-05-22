import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app

def test_index():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200

def test_add_task():
    client = app.test_client()
    res = client.post('/add', data={'title': 'Test Task'}, follow_redirects=True)
    assert res.status_code == 200