import requests

def get_github_user(username):
    if not username:
        return {'error': 'Usuario nao informado'}, 400

    url = f'https://api.github.com/users/{username}'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Levanta exceção para erros HTTP 4xx e 5xx
        data = response.json()

        return {
            'nome': data.get('name'),
            'avatar_url': data.get('avatar_url'),
            'email': data.get('email'),
            'bio': data.get('bio'),
            'seguidores': data.get('followers'),
            'quantidade_repositorios': data.get('public_repos'),
        }, 200

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return {'error': 'Usuario nao encontrado'}, 404
        return {'error': f'Erro HTTP: {http_err}'}, response.status_code

    except requests.exceptions.RequestException as req_err:
        return {'error': f'Erro ao acessar API do GitHub: {str(req_err)}'}, 500

def get_user_repos(username):
    if not username:
        return {'error': 'Usuario nao informado'}, 400

    url = f'https://api.github.com/users/{username}/repos'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Levanta exceção para erros HTTP 4xx e 5xx
        repos = response.json()

        repo_list = [{
            'nome': repo['name'],
            'nome_completo': repo['full_name'],
            'url': repo['html_url']
        } for repo in repos]

        return repo_list, 200

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return {'error': 'Usuario nao encontrado'}, 404
        return {'error': f'Erro HTTP: {http_err}'}, response.status_code

    except requests.exceptions.RequestException as req_err:
        return {'error': f'Erro ao acessar API do GitHub: {str(req_err)}'}, 500