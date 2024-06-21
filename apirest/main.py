import sqlite3
from flask import Flask, jsonify, request, render_template
from api.cnxSqlite import cnxsqlite
from config import configura
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

app.config['MAIL_SERVER'] = 'lau3232435124@gmail.com'
app.config['MAIL_PORT'] = 5000
app.config['MAIL_USE_TLS'] =True 
app.config['MAIL_USERNAME'] = 'lau3232435124@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'

mail=Mail(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Reporte.db'
db =SQLAlchemy(app)

app.route("/citarComite", methods= ['POST'])
def Citar():
    Usuario_id =request.form['identificacion']
    Usuario =Usuario.query.get(Usuario_id)
    if Usuario:
        subject = "Nueva citación"
        body =f"Hola {Usuario.Nombre}, has sido citado a comite el dia"
        

# Ruta para obtener la lista de usuarios registrados
@app.route("/registrarAprendizcoordinacion", methods=['GET'])
def ListaUsuarios():
    try:
        sql = "SELECT * FROM Usuario"
        con = cnxsqlite()
        todo = con.Consultar("./comite.db", sql)
        return jsonify(todo)
    except Exception as e:
        return str(e), 500


# Ruta para registrar un nuevo usuario coordinación
@app.route("/registrarAprendizcoordinacion/i", methods=['POST'])
def CrearUsuario():
    try:
        datos = request.get_json()
        Identificacion = datos['Identificacion']
        Nombre = datos['Nombre']
        Direccion = datos['Direccion']
        Telefono = datos['Telefono']
        Correo = datos['Correo']
        Ficha = datos['Ficha']
        ProgramaFormacion = datos['ProgramaFormacion']
        Rol = datos['Rol']

        sql = "INSERT INTO Usuario (Identificacion, Nombre, Direccion, Telefono, Correo, Ficha, ProgramaFormacion, Rol) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        con = cnxsqlite()
        con.Ejecutar("./comite.db", sql, (Identificacion, Nombre, Direccion, Telefono, Correo, Ficha, ProgramaFormacion, Rol))
        
        return "Datos recibidos correctamente"
    except Exception as e:
        return str(e), 500


# Ruta para obtener la lista de fichas de aprendices
@app.route("/reportarAprendizcoordinacion", methods=['GET'])
def TraerFicha():
    sql = "SELECT Identificacion, Nombre, ProgramaFormacion, Ficha, Direccion, Telefono, Correo FROM Usuario"
    con = cnxsqlite()
    todo = con.Consultar("./comite.db", sql)
    return jsonify(todo)


# Ruta para registrar un nuevo proceso de reporte de aprendices rol coordinación
@app.route("/reportarAprendizcoordinacion/i", methods=['POST'])
def iniciarProceso():
    try:
        datos = request.get_json()
        Ficha = datos.get('Ficha')
        CedulaUsuario = datos.get('CedulaUsuario')
        Nombre = datos.get('Nombre')
        ProgramaFormacion = datos.get('ProgramaFormacion')
        Coordinacion = datos.get('Coordinacion')
        TipoFalta = datos.get('TipoFalta')
        CausasReporte = datos.get('CausasReporte')
        Faltas = datos.get('Faltas')
        FechaHora = datos.get('FechaHora')
        EvidenciaPDF = datos.get('EvidenciaPDF')

        con = sqlite3.connect("./comite.db")
        cur = con.cursor()
        cur.execute("INSERT INTO Reporte (Ficha, CedulaUsuario, Nombre, ProgramaFormacion, Coordinacion, TipoFalta, CausasReporte, Faltas, FechaHora, EvidenciaPDF) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                    (Ficha, CedulaUsuario, Nombre, ProgramaFormacion, Coordinacion, TipoFalta, CausasReporte, Faltas, FechaHora, EvidenciaPDF))
        con.commit()
        con.close()

        return "Proceso de reporte iniciado correctamente"
    except Exception as e:
        return str(e), 500


# Ruta para consultar reportes de aprendices por coordinación
@app.route("/consultarcoordinacion/i", methods=["POST"])
def consultarAprendiz():
    try:
        CedulaUsuario = request.form.get('CedulaUsuario')

        con = sqlite3.connect("./comite.db")
        cur = con.cursor()

        sql = "SELECT * FROM Reporte WHERE CedulaUsuario = ?"
        cur.execute(sql, (CedulaUsuario,))

        Reporte = cur.fetchall()
        con.close()

        if Reporte:
            Reporte_dict = [{
                'IdReporte': row[0],
                'CedulaUsuario': row[1],
                'Nombre': row[2],
                'Ficha': row[3],
                'ProgramaFormacion': row[4],
                'Coordinacion': row[5],
                'TipoFalta': row[6],
                'CausasReporte': row[7],
                'Faltas': row[8],
                'EvidenciaPDF': row[9]
            } for row in Reporte]

            return render_template("busqueda_historial.html", reportes=Reporte_dict)
        else:
            msgitos = "No existen reportes para este aprendiz"
            return render_template("alertas.html", msgito=msgitos)
    except Exception as e:
        return str(e), 500


# Ruta para crear un acta
@app.route("/registrarActa/i", methods=["POST"])
def CrearActa():
    try:
        datos = request.get_json()
        IdActa = datos['IdActa']
        FechaActa = datos['FechaActa']
        Hora = datos['Hora']
        DetallesActa = datos['DetallesActa']
        IdPlanMejora = datos['PlanMejora']

        con = sqlite3.connect("./comite.db")
        cur = con.cursor()

        cur.execute("INSERT INTO Acta (IdActa, FechaActa, Hora, DetallesActa, PlanMejora) VALUES (?, ?, ?, ?, ?)", (IdActa, FechaActa, Hora, DetallesActa, IdPlanMejora))
        con.commit()
        con.close()

        return "Acta creada correctamente"
    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(debug=True, port=configura['PUERTOREST'], host='0.0.0.0')
