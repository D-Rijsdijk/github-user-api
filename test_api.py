from app import create_app
from pytest import fixture
from unittest.mock import patch


@fixture()
def app():
    app = create_app()
    yield app


@fixture()
def client(app):
    return app.test_client()


@patch('services.requests')
def test_should_return_bad_request_to_unknown_user(mock_response, client):
    mock_response.status_code = 404
    mock_response.get.return_value = mock_response
    response = client.get('/users/unknown_user')
    assert response.status_code == 404


def test_should_return_bad_request_when_username_is_not_informed(client):
    response = client.get('/users/')
    assert response.status_code == 400


@patch('services._user_repositories')
@patch('services.requests')
def test_should_return_success_response(user_info, user_repos, client):
    user_info.json.return_value = {
        'name': 'User Name',
        'avatar_url': 'https://avatar.com',
        'email': 'username@gmail.com',
        'bio': 'User bio',
        'followers': 10,
    }
    user_repos.return_value = [
        {
            'name': 'repo1',
            'full_name': 'user/repo1',
            'html_url': 'github.com/user/repo1',
        },
        {
            'name': 'repo2',
            'full_name': 'user/repo2',
            'html_url': 'github.com/user/repo2',
        }
    ]
    user_info.status_code = 200
    user_info.get.return_value = user_info

    response = client.get('/users/username')
    assert response.status_code == 200
    assert response.json.get('quantidade_repositorios') == len(user_repos.return_value)