from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de MariaDB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'turismo'
app.config['MYSQL_PASSWORD'] = 'Panchetos1234'
app.config['MYSQL_DB'] = 'turismo'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        rut = request.form['rut']
        nombre_completo = request.form['nombre_completo']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo_electronico = request.form['correo_electronico']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (rut, nombre_completo, direccion, telefono, correo_electronico) VALUES (%s, %s, %s, %s, %s)",
                    (rut, nombre_completo, direccion, telefono, correo_electronico))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'POST':
        correo_electronico = request.form['correo_electronico']
        mensaje = request.form['mensaje']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO suggestions (correo_electronico, mensaje) VALUES (%s, %s)",
                    (correo_electronico, mensaje))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('suggestions.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        comentario = request.form['comentario']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO comentarios (comentario) VALUES (%s)", [comentario])
        mysql.connection.commit()
        cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.execute("SELECT * FROM suggestions")
    suggestions = cur.fetchall()
    cur.close()
    return render_template('admin.html', users=users, suggestions=suggestions)

@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('admin'))

@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_user(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", [id])
    data = cur.fetchall()
    cur.close()
    return render_template('edit.html', user=data[0])

@app.route('/update/<id>', methods=['POST'])
def update_user(id):
    if request.method == 'POST':
        rut = request.form['rut']
        nombre_completo = request.form['nombre_completo']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo_electronico = request.form['correo_electronico']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE users
            SET rut = %s,
                nombre_completo = %s,
                direccion = %s,
                telefono = %s,
                correo_electronico = %s
            WHERE id = %s
        """, (rut, nombre_completo, direccion, telefono, correo_electronico, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin'))

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

if __name__ == '__main__':
    app.run(debug=True)
