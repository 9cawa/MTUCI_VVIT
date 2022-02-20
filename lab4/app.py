import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="2412564",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/', methods=['POST'])
def login():
    username = request.form.get('username')
    if username == "":
        return "Введите логин!"
    password = request.form.get('password')
    if password == "":
        return "Введите пароль!"
    try:
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
    except Exception as E:
        print(E)
        return "Вы не зарегистрированы!"


if __name__ == '__main__':
    app.run(debug=True)
