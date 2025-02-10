import sqlite3
from flask import(
    Flask,
    redirect,
    render_template,
    request,
    jsonify
)


app = Flask(__name__)


def create_db():
    with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                password TEXT
            )
        """)
        connection.commit()


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name', '')
    email = data.get('email', '')
    password = data.get('password', '')



    with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        connection.commit()

    return jsonify({"message": "Пользователь зарегистрирован успешно"}), 201

if __name__ == '__main__':
    create_db()
    app.run(debug=True)
