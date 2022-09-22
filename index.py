#1.USO DE SANGRÍA
#2.EVITAR COMENTARIOS OVBIOS
#3.AGRUPACIÓN DE CÓDIGOS
#4.EVITAR ANIDAMIENTO PROFUNDO
#5.PONER EN MAYUSCULAS LAS PALABRAS ESPECIALES DE SQL
#6.LIMITE DE LONGITUD DE LA LINEA

from flask import Flask
from flask import render_template, request
from flask_mysqldb import MySQL




app= Flask(__name__)

#Configuración de nocexión a base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '3306'
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app)





#LLAMADA A LAS RUTAS DE LAS PAGINAS 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/La_escuela')
def escuela():
    return render_template('La_escuela.html')

@app.route('/Director')
def director():
    return render_template('Director.html')    

@app.route('/MisionyVision')
def mision_vision():
    return render_template('Mision_vision.html') 
 
@app.route('/Objetivos')
def objetivos():
    return render_template('Objetivo.html') 

@app.route('/Plan_Estudios')
def plan_estudios():
    return render_template('Plan_estudios.html')

@app.route('/Grados_academicos')
def grados_academicos():
    return render_template('Grados_academicos.html')

@app.route('/Login')
def Login():
    return render_template('Login.html')





#agregar contacto
@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
       fullname = request.form['fullname']
       phone = request.form['phone']
       email = request.form['email']
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', 
                    (fullname, phone, email))
       mysql.connection.commit()
       return render_template('home.html')
       


if __name__ == '__main__':
    app.run(debug=True) 