import pytest
from app import app

# Utilizamos o pytest.fixture para criar um cliente de teste para a aplicação Flask
@pytest.fixture
def client():
    # Configura a aplicação para o modo de teste
    app.config['TESTING'] = True
    # Cria um cliente de teste usando o contexto 'with'
    with app.test_client() as client:
        # 'yield' fornece o cliente para os testes e depois limpa os recursos
        yield client

# Teste para verificar se a rota principal '/' responde corretamente
def test_index(client):
    """Testa se a rota principal responde com status 200 e contém o texto esperado."""
    # Faz uma requisição GET para a rota '/'
    response = client.get('/')
    # Verifica se o status da resposta é 200 (OK)
    assert response.status_code == 200
    # Verifica se o conteúdo da resposta contém a string esperada
    assert b"Gerador de Fake Users" in response.data

# Teste para verificar se a rota '/gerar_usuarios' funciona corretamente sem parâmetros adicionais
def test_gerar_usuarios(client):
    """Testa a geração de usuários com parâmetros padrão."""
    # Dados enviados na requisição POST
    data = {
        'quantidade': 5  # Número de usuários a serem gerados
    }
    # Faz uma requisição POST para a rota '/gerar_usuarios' com os dados fornecidos
    response = client.post('/gerar_usuarios', data=data)
    # Verifica se o status da resposta é 200 (OK)
    assert response.status_code == 200
    # Obtém os dados JSON da resposta
    usuarios = response.get_json()
    # Verifica se a quantidade de usuários retornados é igual à solicitada
    assert len(usuarios) == 5
    # Verifica se cada usuário possui os campos esperados
    for usuario in usuarios:
        assert 'nome' in usuario
        assert 'sobrenome' in usuario
        assert 'email' in usuario
        assert 'endereco' in usuario
        assert 'telefone' in usuario
        assert 'data_nascimento' in usuario
        assert 'username' in usuario

# Teste para verificar se a geração de usuários funciona com parâmetros personalizados
def test_gerar_usuarios_com_parametros(client):
    """Testa a geração de usuários com parâmetros personalizados."""
    # Dados enviados na requisição POST
    data = {
        'quantidade': 3,
        'genero': 'female',
        'dominio': 'exemplo.com;teste.com'
    }
    # Faz uma requisição POST para a rota '/gerar_usuarios' com os dados fornecidos
    response = client.post('/gerar_usuarios', data=data)
    # Verifica se o status da resposta é 200 (OK)
    assert response.status_code == 200
    # Obtém os dados JSON da resposta
    usuarios = response.get_json()
    # Verifica se a quantidade de usuários retornados é igual à solicitada
    assert len(usuarios) == 3
    # Verifica se cada usuário possui os campos esperados e os valores correspondentes
    for usuario in usuarios:
        assert 'nome' in usuario
        assert 'sobrenome' in usuario
        assert 'email' in usuario
        assert 'endereco' in usuario
        assert 'telefone' in usuario
        assert 'data_nascimento' in usuario
        assert 'username' in usuario
        # Verifica se o gênero é feminino (opcional, pois usamos nomes aleatórios)
        # Verifica se o domínio do e-mail é um dos domínios fornecidos
        assert any(dominio in usuario['email'] for dominio in ['exemplo.com', 'teste.com'])

# Teste para verificar o tratamento de erros quando uma quantidade inválida é fornecida
def test_gerar_usuarios_quantidade_invalida(client):
    """Testa o comportamento da API quando uma quantidade inválida é fornecida."""
    data = {
        'quantidade': -5  # Quantidade inválida (negativa)
    }
    response = client.post('/gerar_usuarios', data=data)
    # Verifica se o status da resposta é 400 (Bad Request)
    assert response.status_code == 400
    # Verifica se a mensagem de erro está presente na resposta
    erro = response.get_json()
    assert 'erro' in erro
    assert erro['erro'] == 'Quantidade deve ser entre 1 e 100'

# Teste para verificar o tratamento de erros quando a quantidade não é um número
def test_gerar_usuarios_quantidade_nao_numero(client):
    """Testa o comportamento da API quando a quantidade não é um número."""
    data = {
        'quantidade': 'abc'  # Quantidade inválida (não numérica)
    }
    response = client.post('/gerar_usuarios', data=data)
    # Verifica se o status da resposta é 400 (Bad Request)
    assert response.status_code == 400
    # Verifica se a mensagem de erro está presente na resposta
    erro = response.get_json()
    assert 'erro' in erro
    assert erro['erro'] == 'Quantidade inválida'

# Teste para verificar o comportamento quando parâmetros opcionais não são fornecidos
def test_gerar_usuarios_sem_parametros_opcionais(client):
    """Testa a geração de usuários sem fornecer parâmetros opcionais."""
    data = {
        'quantidade': 2
        # Não fornecemos 'genero' nem 'dominio'
    }
    response = client.post('/gerar_usuarios', data=data)
    assert response.status_code == 200
    usuarios = response.get_json()
    assert len(usuarios) == 2
    for usuario in usuarios:
        assert 'nome' in usuario
        assert 'sobrenome' in usuario
        assert 'email' in usuario
        # Podemos verificar se o domínio do e-mail está na lista padrão de domínios
        assert any(dominio in usuario['email'] for dominio in ['exemplo.com', 'email.com', 'dominio.com'])

# Teste para verificar se a rota '/gerar_usuarios' retorna um erro quando nenhum dado é enviado
def test_gerar_usuarios_sem_dados(client):
    """Testa o comportamento da API quando nenhum dado é enviado na requisição."""
    response = client.post('/gerar_usuarios')
    # Verifica se o status da resposta é 400 (Bad Request)
    assert response.status_code == 400
    # Verifica se o tipo de conteúdo é JSON
    assert response.content_type == 'application/json'
    erro = response.get_json()
    assert erro is not None, "Resposta não é um JSON válido"
    assert 'erro' in erro
    assert erro['erro'] == 'Quantidade inválida'
