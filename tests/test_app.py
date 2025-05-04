from http import HTTPStatus


def test_profile(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Paula',
            'usermail': 'Paula@gmail.com',
            'userpassword': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Paula',
        'usermail': 'Paula@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Paula',
                'usermail': 'Paula@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Paula22',
            'usermail': 'Paula22@example.com',
            'userpassword': 'secret1',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Paula22',
        'usermail': 'Paula22@example.com',
        'id': 1,
    }


def test_read_user_expe(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'Paula22',
        'usermail': 'Paula22@example.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User Deleted'}
