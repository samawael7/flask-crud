import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app, init_db

def test_index():
    app.config['TESTING'] = True
    with app.app_context():
        init_db()
    with app.test_client() as client:
        res = client.get('/')
        assert res.status_code == 200

def test_add_task():
    app.config['TESTING'] = True
    with app.app_context():
        init_db()
    with app.test_client() as client:
        res = client.post('/add', data={'title': 'Test Task'}, follow_redirects=True)
        assert res.status_code == 200