import requests
from requests.exceptions import RequestException

GITHUB_BASE_URL = 'https://api.github.com'


def get_github_user(username: str) -> tuple[dict, int]:
    try:
        response = requests.get(f"{GITHUB_BASE_URL}/users/{username}")
        if response.status_code == 200:
            data = response.json()
            repos = _user_repositories(username)
            return {
                'nome': data.get('name'),
                'avatar_url': data.get('avatar_url'),
                'email': data.get('email'),
                'bio': data.get('bio'),
                'seguidores': data.get('followers'),
                'quantidade_repositorios': len(repos),
                'repositorios': repos
            }, response.status_code
        if response.status_code == 404:
            return {'error': 'Usuario nao encontrado'}, response.status_code
        return {'error': 'Erro ao acessar API do GitHub'}, response.status_code

    except requests.exceptions.RequestException as req_err:
        return {'error': f'Erro ao acessar API do GitHub: {str(req_err)}'}, 500


def _user_repositories(username: str) -> list[dict]:
    try:
        response = requests.get(f"{GITHUB_BASE_URL}/users/{username}/repos")
        if response.status_code == 200:
            repos = response.json()
            return [
                {
                    'nome': repo.get('name'),
                    'nome_completo': repo.get('full_name'),
                    'url': repo.get('html_url')
                } for repo in repos
            ]
        raise RequestException
    except RequestException:
        raise