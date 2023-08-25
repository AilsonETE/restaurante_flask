from flask import Flask
from flask import render_template
import sqlite3



#cria o objeto app
app = Flask(__name__ , static_folder='static')


# conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('database\sqlite.db')
    conn.row_factory = sqlite3.Row
    return conn

# cria a rota index
@app.route("/")
def index():
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    pratos = conn.execute('SELECT * FROM pratos').fetchall()
    conn.close()
    return render_template('index.html', categorias=categorias, pratos=pratos)

app.run(debug=True)