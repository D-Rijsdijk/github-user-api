import requests

def get_github_user(username):
    if not username: 
        return {'error': 'Usário não informado'}, 400 
    
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 404:
        return {'error': 'Usuário não encontrado'}, 404
    
    data = response.json()
    return{
        'nome': data.get('name'),
        'avatar_url': data.get('avatar_url'),
        'email': data.get('email'),
        'bio': data.get('bio'),
        'seguidores': data.get('followers'),
        'quantidade_repositorios': data.get('public_repos'),
    }, 200

    def get_user_repos(username):
        url = 'https://api.github.com/users/{username}/repos'
        response = requests.get(url)

        if response.status_code == 404:
            return {'error': 'Usuário não encontrado'}