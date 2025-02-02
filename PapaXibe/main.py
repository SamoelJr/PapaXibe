from unittest import result
from colorama import Cursor
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(host="db4free.net", user="admin_uniz", password="senha123", database="proj_integrado")
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS User")

sql = '''CREATE TABLE User(
    nome CHAR(50) NOT NULL,
    contato CHAR(50) NOT NULL,
    senha CHAR(50) NOT NULL,
    preco CHAR(50) NOT NULL,
    descricao CHAR(50) NOT NULL
)'''

cursor.execute(sql)

db.close()

""" Configurações para pagina de login/delete da aplicação """
# Apagar algo do banco de dados
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        ##########AP
        db = pymysql.connect(host="db4free.net", user="admin_uniz", password="senha123", database="proj_integrado")
        cursor = db.cursor()

        sql = 'DROP * FROM User'

        cursor.execute(sql)

        return render_template("index.html")
    else:
        contato = request.form.get("contato")
        print(contato)
        return render_template("list.html")


"""Configurações para pagina de list da aplicação"""
# fazer um while com jinja que list todos os anúncios do banco de dados
@app.route("/")
def list():

    db = pymysql.connect(host="db4free.net", user="admin_uniz", password="senha123", database="proj_integrado")
    cursor = db.cursor()

    nomesepreco = []

    lista = []

    sql = 'SELECT * FROM User'

    cursor.execute(sql)

    usuarios = cursor.fetchall()
    print(usuarios)
    for row in usuarios:

        lista = [row[0], row[3]]

        nomesepreco.append(lista)
        print(nomesepreco)

    print(nomesepreco)

    db.close()
    return render_template("list.html", dados=nomesepreco)


"""Configurações para pagina de cadastro da aplicação"""
# Salvar dados no banco de dados
@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':

        nome = request.form.get("nome")
        senha = request.form.get("senha")
        preçoparaotransporte = request.form.get("preçoparaotransporte")
        descricao = request.form.get("descricao")
        emailounumerodecelular = request.form.get("emailounumerodecelular")

        print(nome, senha, preçoparaotransporte, descricao, emailounumerodecelular)

        db = pymysql.connect(host="db4free.net", user="admin_uniz", password="senha123", database="proj_integrado")
        cursor = db.cursor()

        sql = f"""INSERT INTO User(nome, contato, senha, descricao, preco)
                    VALUES ('{nome}', '{emailounumerodecelular}', '{senha}', '{descricao}', '{preçoparaotransporte}')"""

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()

        return render_template("cadastrar.html")
    else:
        return render_template("cadastrar.html")


"""Configurações para pagina de exibição da aplicação"""
# Mostrar os dados dos anúncios salvos no banco de dados
@app.route("/exibir")
def exibir():

    ##########AP
    db = pymysql.connect(host="db4free.net", user="admin_uniz", password="senha123", database="proj_integrado")
    cursor = db.cursor()

    user = []

    lista = []

    sql = 'SELECT * FROM User'

    cursor.execute(sql)

    usuario = cursor.fetchall()
    print(usuario)
    for row in usuario:

        lista = [row[0], row[3]]

        user.append(lista)
        print(user)

    print(user)

    db.close()

    return render_template("exibir.html", dados=user)

if __name__ == "__main__":
    app.run(debug=True)