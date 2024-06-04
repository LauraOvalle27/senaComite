import sqlite3
from flask import Flask, jsonify, redirect, render_template,request, url_for, render_template_string
import json
#from services.apicnx import cnxsqlite
from api.cnxSqlite import cnxsqlite  
from config import configura 
app=Flask(__name__)

@app.route("/registrarAprendizcoordinacion")
def ListaAmbiente():
    sql = "SELECT * FROM Usuario" 
    con = cnxsqlite()
    todo = con.Consultar("./comite.db", sql)
    return json.dumps(todo)
    




"""
@app.route("/")
def inicio():
    return "Hola"

@app.route("/usua/cc")

@app.route("/usua/to")
def ListaUsuario():
    sql="select * from USUA"
    con=cnxsqlite()   
    todo=con.Consultar("./comite.db",sql)
    return json.dumps(todo)
@app.route("/usua/<id>")
def ListaUnUsuario(id):
    sql="select * from USUA where IDUSUA="+str(id)
    con=cnxsqlite()
    todo=con.ConsultarUno("./comite.db",sql)
    return json.dumps(todo)
"""
@app.route("/registrarAprendizcoordinacion/i",methods = ['POST'])
def CrearUsuario(): 
    datos=request.get_json()
    Identificacion=datos['Identificacion']
    Nombre=datos['Nombre']
    Direccion=datos['Direccion']
    Telefono=datos['Telefono']
    Correo=datos['Correo']
    Ficha=datos['Ficha']
    ProgramaFormacion=datos['ProgramaFormacion']
    Rol=datos['Rol']

    sql="insert into Usuario (Identificacion, Nombre,Direccion,Telefono,Correo,Ficha,ProgramaFormacion,Rol) values('"+Identificacion+"','"+Nombre+"','"+Direccion+"', '"+Telefono+"', '"+Correo+"', '"+Ficha+"', '"+ProgramaFormacion+"', '"+Rol+"')"
    con=cnxsqlite() 
    todo=con.Ejecutar("./comite.db",sql)
    return"Datos recibidos correctamente"

"""
@app.route("/registrarAprendizinstructor/i",methods = ['POST'])
def CrearUsuarioinst(): 
    datos=request.get_json()
    Identificacion=datos['Identificacion']
    Nombre=datos['Nombre']
    Direccion=datos['Direccion']
    Telefono=datos['Telefono']
    Correo=datos['Correo']
    Ficha=datos['Ficha']
    ProgramaFormacion=datos['ProgramaFormacion']
    Rol=datos['Rol']

    sql="insert into Usuario (Identificacion, Nombre,Direccion,Telefono,Correo,Ficha,ProgramaFormacion,Rol) values('"+Identificacion+"','"+Nombre+"','"+Direccion+"', '"+Telefono+"', '"+Correo+"', '"+Ficha+"', '"+ProgramaFormacion+"', '"+Rol+"')"
    con=cnxsqlite() 
    todo=con.Ejecutar("./comite.db",sql)
    return"Datos recibidos correctamente"

 """


@app.route("/reportarAprendizcoordinacion/i", methods=['POST'])
def iniciarProceso():
    # Obtener los datos del JSON recibido
    datos = request.get_json()
    # Extraer los datos del JSON
    Ficha = datos.get('Ficha')
    CedulaUsuario = datos.get('CedulaUsuario')
    Nombre = datos.get('Nombre')
    ProgramaFormacion = datos.get('ProgramaFormacion')
    Coordinacion = datos.get('Coordinacion')
    TipoFalta = datos.get('TipoFalta')
    CausasReporte = datos.get('CausasReporte')
    Faltas = datos.get('Faltas')
    EvidenciaPDF = datos.get('EvidenciaPDF')
    
    # Imprimir los datos recibidos en la consola
    print(f"Datos recibidos: Ficha={Ficha}, CedulaUsuario={CedulaUsuario}, Nombre={Nombre}, ProgramaFormacion={ProgramaFormacion}, Coordinacion={Coordinacion}, TipoFalta={TipoFalta}, CausasReporte={CausasReporte}, Faltas={Faltas},EvidenciaPDF={EvidenciaPDF}")

    # Insertar los datos en la base de datos
    con = sqlite3.connect("./comite.db")
    cur = con.cursor()
    # Aquí insertamos los datos sin incluir el campo IdReporte, que se autoincrementará automáticamente
    cur.execute("INSERT INTO Reporte (Ficha, CedulaUsuario, Nombre, ProgramaFormacion, Coordinacion, TipoFalta, CausasReporte, Faltas, EvidenciaPDF) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (Ficha, CedulaUsuario, Nombre, ProgramaFormacion, Coordinacion, TipoFalta, CausasReporte, Faltas, EvidenciaPDF))
    con.commit()
    con.close()


@app.route("/reportarAprendizinstructor/i", methods=['POST'])
def iniciarProcesoInstructor():
    datos = request.get_json()
    IdReporte = datos.get('IdReporte')
    Ficha = datos.get('Ficha')
    CedulaUsuario = datos.get('CedulaUsuario')
    Nombre = datos.get('Nombre')
    ProgramaFormacion = datos.get('ProgramaFormacion')
    Coordinacion = datos.get('Coordinacion')
    TipoFalta = datos.get('TipoFalta')
    CausasReporte = datos.get('CausasReporte')
    Faltas = datos.get('Faltas')
    EvidenciaPDF = datos.get('EvidenciaPDF')

    # Imprimir los datos recibidos en la consola
    print(f"Datos recibidos: Ficha={Ficha}, CedulaUsuario={CedulaUsuario}, Nombre={Nombre}, ProgramaFormacion={ProgramaFormacion}, Coordinacion={Coordinacion}, TipoFalta={TipoFalta}, CausasReporte={CausasReporte}, Faltas={Faltas}, EvidenciaPDF={EvidenciaPDF}")

    # Insertar los datos en la base de datos
    con = sqlite3.connect("./comite.db")
    cur = con.cursor()
    # Aquí insertamos los datos sin incluir el campo IdReporte, que se autoincrementará automáticamente
    cur.execute("INSERT INTO Reporte (IdReporte, Ficha, CedulaUsuario, Nombre, ProgramaFormacion, Coordinacion, TipoFalta, CausasReporte, Faltas,EvidenciaPDF) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (IdReporte, Ficha, CedulaUsuario, Nombre, ProgramaFormacion, Coordinacion, TipoFalta, CausasReporte, Faltas, EvidenciaPDF))
    con.commit()
    con.close()



@app.route("/consultarcoordinacion/i", methods=["POST"])
def consultarAprendiz():
    CedulaUsuario=request.form.get('CedulaUsuario')

    con = sqlite3.connect("./comite.db")
    cur = con.cursor()

    sql="select * from Reporte where CedulaUsuario = ?"
    cur.execute(sql, (CedulaUsuario,))

    Reporte = cur.fetchall()

    print("Datos obtenidos de la base de datos:", Reporte)

    con.commit()
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

    


        return render_template("busqueda_historial.html", reportes= Reporte_dict)
        

    else:

        msgitos="No existen reportes para este aprendiz" 
        return render_template("alertas.html",msgito=msgitos)


"""
@app.route("/usua/u",methods = ['PUT'])
def EditaUsuario(): 
    datos=request.get_json()
    id=datos['IDUSUARIO']
    ape=datos['APELLIDO']
    nom=datos['NOMBRE']
    sql="update USUA set NOMBRE='"+nom+"',APELLIDO='"+ape+"' where IDUSUA="+str(id)
    con=cnxsqlite()
    todo=con.Ejecutar("./comite.db",sql)

    return "OK"
@app.route("/usua/d/<id>",methods = ['DELETE'])
def BorrarUsuario(id): 
    sql="delete from USUA where IDUSUA="+str(id)
    con=cnxsqlite()
    todo=con.Ejecutar("./comite.db",sql)
    return "OK"
@app.route("/usua/menus",methods=['GET'])
def VerMenu():
    sql="select * from MODULOS"
    con=cnxsqlite()
    todo=con.ConsultarJson("./comite.db",sql)
    return jsonify(todo)
"""
if __name__=='__main__':
    app.run(debug=True,port=configura['PUERTOREST'],host='0.0.0.0')
