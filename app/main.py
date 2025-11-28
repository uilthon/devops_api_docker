from flask import Flask, request, jsonify
import mysql.connector
import os, time

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'apppass')
DB_NAME = os.getenv('DB_NAME', 'appdb')

def get_db_connection(retries=5, delay=2):
    for i in range(retries):
        try:
            return mysql.connector.connect(
                host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
            )
        except Exception as e:
            if i == retries - 1:
                raise
            time.sleep(delay)

@app.route('/users', methods=['GET'])
def list_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json(force=True)
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'name and email required'}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    conn.commit()
    last_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({'id': last_id, 'name': data['name'], 'email': data['email']}), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json(force=True)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (data.get('name'), data.get('email'), id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'updated'}), 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'deleted'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
