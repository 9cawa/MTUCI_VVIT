import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="2412564",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')
            if username == "":
                return "Введите логин!"
            password = request.form.get('password')
            if password == "":
                return "Введите пароль!"
            try:
                cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s",
                               (str(username), str(password)))
                records = list(cursor.fetchall())
                return render_template('account.html', full_name=records[0][1])
            except Exception as E:
                print(E)
                return "Вы не зарегистрированы!"

        elif request.form.get("registration"):
            return redirect("/registration/")
    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        if name == "":
            return "Введите своё полное имя!"

        login = request.form.get('login')
        if login == "":
            return "Введите логин!"

        password = request.form.get('password')
        if password == "":
            return "Введите пароль!"

        try:
            cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s,%s,%s);',
                        (str(name), str(login), str(password)))
            conn.commit()
            return redirect('/login/')
        except Exception as E:
            print(E)
            return "Пользователь с таким логином уже зарегистрирован!"
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)
