from app import app


def test_index_get_renders_page():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert b'<form' in response.data


def test_favicon_route_serves_icon():
    client = app.test_client()
    response = client.get('/favicon.ico')

    assert response.status_code == 200
    assert response.mimetype == 'image/vnd.microsoft.icon'


def test_hello_post_with_name_renders_hello_template():
    client = app.test_client()
    response = client.post('/hello', data={'name': 'Alice'})

    assert response.status_code == 200
    assert b'Alice' in response.data


def test_hello_post_without_name_redirects_to_index():
    client = app.test_client()
    response = client.post('/hello', data={'name': ''})

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/')
