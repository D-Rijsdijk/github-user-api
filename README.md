# GitHub User Info API

Este projeto é uma API que permite buscar informações de usuários do GitHub, incluindo dados pessoais e repositórios. A API é construída usando Flask e faz requisições à API do GitHub para obter os dados necessários.

## Requisitos

- Python 3 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Executando a API

1. **Inicie o servidor Flask:**

   ```bash
   python app.py
   ```

2. **O servidor estará rodando em:**
   
   ```
   http://localhost:5000
   ```

3. **Teste a API:**

   **Buscar informações de um usuário:**
   
   ```bash
   curl -X GET http://localhost:5000/users/{username}
   ```
   
   Substitua `{username}` pelo nome de usuário do GitHub que deseja buscar.

   **Erro quando o nome de usuário não é informado:**
   
   ```bash
   curl -X GET http://localhost:5000/users/
   ```
   
   A API retornará um erro 400 com a mensagem "Usuario nao informado".

## Estrutura do Projeto

- `app.py`: Ponto de entrada da aplicação. Inicia o servidor Flask.
- `routes.py`: Define as rotas da API.
- `services.py`: Contém a lógica para fazer requisições à API do GitHub e processar os dados.
- `test_api.py`: Testes unitários para a API.
- `openapi.yaml`: Especificação OpenAPI para documentação da API.
- `requirements.txt`: Lista de dependências do projeto.

## Testes

Para executar os testes, utilize o seguinte comando:

```bash
pytest test_api.py
```

## Documentação da API

A documentação da API está disponível no arquivo `openapi.yaml`. Você pode visualizá-la usando ferramentas como o Swagger Editor.

## Exemplo de Resposta

### Sucesso (200)

```json
{
  "nome": "User Name",
  "avatar_url": "https://avatar.com",
  "email": "username@gmail.com",
  "bio": "User bio",
  "seguidores": 10,
  "quantidade_repositorios": 2,
  "repositorios": [
    {
      "nome": "repo1",
      "nome_completo": "user/repo1",
      "url": "https://github.com/user/repo1"
    },
    {
      "nome": "repo2",
      "nome_completo": "user/repo2",
      "url": "https://github.com/user/repo2"
    }
  ]
}
```

### Erro (400)

```json
{
  "error": "Usuario nao informado"
}
```

### Erro (404)

```json
{
  "error": "Usuario nao encontrado"
}
```

### Erro (500)

```json
{
  "error": "Erro ao acessar API do GitHub: <mensagem de erro>"
}
```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:

   ```bash
   git checkout -b feature/nova-feature
   ```

3. Commit suas mudanças:

   ```bash
   git commit -m 'Adicionando nova feature'
   ```

4. Push para a branch:

   ```bash
   git push origin feature/nova-feature
   ```

5. Abra um Pull Request.
