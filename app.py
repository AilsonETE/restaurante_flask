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

# Rota para o painel de administração
@app.route("/admin")
def admin_panel():    
    return render_template('admin/painel.html')

# Rota para listar categorias
@app.route("/admin/listar_categorias")
def listar_categorias():
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    conn.close()
    return render_template('admin/listar_categorias.html', categorias=categorias)

# Rota para cadastrar categoria
@app.route("/admin/cadastrar_categoria")
def cadastrar_categoria():
    # Implemente o código para cadastrar categoria
    return render_template('admin/cadastrar_categoria.html')

# Rota para excluir categoria
@app.route("/admin/excluir_categoria")
def excluir_categoria():
    # Implemente o código para excluir categoria
    return render_template('admin/excluir_categoria.html')



# cria a rota index
@app.route("/")
def index():
    conn = get_db_connection()
    categorias = conn.execute('SELECT * FROM categorias').fetchall()
    pratos = conn.execute('SELECT * FROM pratos').fetchall()
    conn.close()
    return render_template('index.html', categorias=categorias, pratos=pratos)

app.run(debug=True)