from flask import Flask, request, jsonify, render_template
import random
from datetime import datetime, timedelta
import names  # Biblioteca para gerar nomes reais
import re #expressões regulares

app = Flask(__name__)

# Listas de domínios e outros dados
dominios = ["exemplo.com", "email.com", "dominio.com"]
ruas = ["Rua A", "Avenida B", "Travessa C", "Alameda D"]
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre"]
estados = ["SP", "RJ", "MG", "RS"]

def gerar_data_nascimento():
    # Gera uma data de nascimento aleatória entre 18 e 60 anos atrás
    start_date = datetime.now() - timedelta(days=365*60)  # 60 anos atrás
    end_date = datetime.now() - timedelta(days=365*18)    # 18 anos atrás
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%d/%m/%Y")

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/gerar_usuarios', methods=['POST'])
def gerar_usuarios():
    try:
        quantidade = int(request.form['quantidade'])
        if quantidade <= 0 or quantidade > 100:
            return jsonify({"erro": "Quantidade deve ser entre 1 e 100"}), 400
    except (ValueError, TypeError, KeyError):
        return jsonify({"erro": "Quantidade inválida"}), 400

    genero_selecionado = request.form.get('genero', 'both')
    dominio_personalizado = request.form.get('dominio')

    if dominio_personalizado:
        # Dividir a string de domínios por vírgulas ou ponto e vírgula
        dominios_utilizados = re.split(r'[;,]', dominio_personalizado)
        # Limpar cada domínio, removendo espaços e '@' iniciais
        dominios_utilizados = [dom.strip().lstrip('@') for dom in dominios_utilizados if dom.strip()]
    else:
        dominios_utilizados = dominios

    usuarios = []

    for _ in range(quantidade):
        # Determina o gênero do nome a ser gerado
        if genero_selecionado == 'both':
            genero = random.choice(['male', 'female'])
        else:
            genero = genero_selecionado

        # Gera um nome completo realista
        nome_completo = names.get_full_name(gender=genero)
        nome, sobrenome = nome_completo.split(' ', 1)

        # Gera outros dados do usuário
        dominio = random.choice(dominios_utilizados)
        email = f"{nome.lower()}.{sobrenome.lower().replace(' ', '')}@{dominio}"
        endereco = {
            "rua": f"{random.choice(ruas)}, {random.randint(1, 1000)}",
            "cidade": random.choice(cidades),
            "estado": random.choice(estados),
            "cep": f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"
        }
        telefone = f"({random.randint(10, 99)}) {random.randint(90000, 99999)}-{random.randint(1000, 9999)}"
        data_nascimento = gerar_data_nascimento()
        username = f"{nome[0].lower()}{sobrenome.lower().split(' ')[-1]}{random.randint(1, 99)}"

        usuarios.append({
            "nome": nome,
            "sobrenome": sobrenome,
            "email": email,
            "endereco": endereco,
            "telefone": telefone,
            "data_nascimento": data_nascimento,
            "username": username
        })

    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)
