import os
from flask import Flask, jsonify, request
from app.crud import list_users, create_user, init_db

app = Flask(__name__)

# Detecta execução no GitHub Actions
is_github_ci = os.getenv("GITHUB_ACTIONS") == "true"

# Se NÃO estiver no GitHub Actions → conecta ao banco
if not is_github_ci:
    init_db()


@app.route("/")
def home():
    return jsonify({"message": "API funcionando!"}), 200


# Rota GET para listar usuários
@app.route("/users", methods=["GET"])
def get_users():
    try:
        users = list_users()
        return jsonify(users), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Erro ao consultar usuários"}), 500


# Rota POST para criar novo usuário
@app.route("/users", methods=["POST"])
def post_user():
    try:
        data = request.get_json()
        create_user(data["name"], data["email"])
        return jsonify({"message": "Usuário criado!"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error": "Erro ao criar usuário"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
