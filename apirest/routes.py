import sqlite3
from flask import Flask, jsonify,request,redirect, url_for
import json,requests
from flask import render_template
from services.apicnx import Usuario   
from config import configura    
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

########## inicio

@app.route('/')
def index():
    return redirect (url_for("loginUsuarios"))

@app.route('/login')
def loginUsuarios():
    return render_template ("login.html")


##### Routes Coordinación


# Ruta de la página de Inicio rol coordinación 


@app.route('/iniciocoordinacion')
def incioCoordinacion():
    return render_template("inicio_coordinacion.html")


#Ruta para Registrar aprendiz rol coordinación

@app.route("/registrarAprendizcoordinacion/",methods=["GET","POST"])
def registrarAprendizCoordinacion():
    return render_template("registrar_coordinacion.html", N=0)

@app.route("/registrarAprendizcoordinacion/<id>",methods=["GET","POST"])
def registrarCoordinacion2(id=0):
    return render_template("registrar_coordinacion.html", N=id)


@app.route("/registrarAprendizcoordinacion/i",methods=["POST"])
def registrarCoordinacion():
    Identificacion=request.form.get('Identificacion')
    Nombre=request.form.get('Nombre')
    Direccion=request.form.get('Direccion')
    Telefono=request.form.get('Telefono')
    Correo=request.form.get('Correo')
    Ficha=request.form.get('Ficha')
    ProgramaFormacion=request.form.get('ProgramaFormacion')
    Rol=request.form.get('Rol')
    u1= Usuario("http://127.0.0.1:5000/registrarAprendizcoordinacion")
    datos={
        "Identificacion":Identificacion, "Nombre":Nombre,"Direccion":Direccion, "Telefono":Telefono, "Correo":Correo, "Ficha":Ficha, "ProgramaFormacion":ProgramaFormacion, "Rol":Rol
    }
    u1.Inserte(datos)
    id=0
    msgitos="Usuario creado satisfactoriamente" 
    print(datos)
    return render_template("alertas.html",msgito=msgitos)



# Ruta para traer las fichas rol coordinación


@app.route("/reportarAprendizcoordinacion" ,methods=["GET"])
def reportarCoordinacion():
    f = requests.get("http://127.0.0.1:5000/reportarAprendizcoordinacion")
    fichas = f.json()
    print(fichas)
    
    return render_template("reportar_coordinacion.html", fichas=fichas)



@app.route("/reportarAprendizcoordinacion/" ,methods=["GET","POST"])
def reportarCoordinacion2():
    f = requests.get("http://127.0.0.1:5000/reportarAprendizcoordinacion")
    fichas = f.json()
    print(fichas)
    return render_template("reportar_coordinacion.html", fichas=fichas)

# Ruta para guardar el reporte del aprendiz rol coordinación

@app.route("/reportarAprendizcoordinacion/i", methods = ['POST'])
def iniciarCoordinacion():
    Ficha=request.form.get('Ficha')
    CedulaUsuario=request.form.get('CedulaUsuario')
    Nombre=request.form.get('Nombre')
    ProgramaFormacion=request.form.get('ProgramaFormacion')
    Coordinacion=request.form.get('Coordinacion')
    TipoFalta=request.form.get('TipoFalta')
    CausasReporte=request.form.get('CausasReporte')
    Faltas=request.form.get('Faltas')
    FechaHora=request.form.get('FechaHora')
    EvidenciaPDF=request.form.get('EvidenciaPDF')
    

    u2= Usuario("http://127.0.0.1:5000/reportarAprendizcoordinacion")

    datos={"Ficha":Ficha, "CedulaUsuario": CedulaUsuario, "Nombre": Nombre, "ProgramaFormacion": ProgramaFormacion, "Coordinacion": Coordinacion, "TipoFalta": TipoFalta, "CausasReporte": CausasReporte, "Faltas":Faltas, "FechaHora":FechaHora, "EvidenciaPDF": EvidenciaPDF}

    u2.Inserte(datos)
    id=0
    msgitos="Reporte creado satisfactoriamente" 
    print(datos)
    return render_template("alertas.html",msgito=msgitos)

# Ruta para mostrar los Procesos pendientes rol coordinación 

@app.route("/procesosPendientescoordinacion")
def procesosPendientes():
    return render_template("procesos_coordinacion.html")


@app.route("/procesosPendientescoordinacion/i", methods=["GET"])
def procesosCoordinacion():

    con = sqlite3.connect("./comite.db")
    cur = con.cursor()

    sql="select * from Reporte"
    cur.execute(sql,)

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

    


        return render_template("procesos_coordinacion.html", reportes= Reporte_dict)
        

    else:

        msgitos="No existen reportes para este aprendiz" 
        return render_template("alertas.html",msgito=msgitos)


# Ruta para relizar la citación del aprendiz rol coordinación 

@app.route("/citacioncoordinacion")
def citacion():
    return render_template("citacion_coordinacion.html")

# Ruta para Consultar Historial del aprendiz rol coordianción 

@app.route("/consultarcoordinacion/" ,methods=["GET","POST"])
def historialCoordinacion():
    return render_template("consultar_coordinacion.html", N=0)

@app.route("/consultarcoordinacion/" ,methods=["GET","POST"])
def historialCoordinacion2(id=0):
    return render_template("consultar_coordinacion.html", N=id)

@app.route("/resultadoHistorial/")
def resultadoHistorial():
    return render_template("busqueda_historial.html")


@app.route("/consultarcoordinacion/i", methods=["POST"])
def consultarAprendiz():
    CedulaUsuario=request.form.get('CedulaUsuario')

    con = sqlite3.connect("./comite.db")
    cur = con.cursor()

    sql="select * from Reporte where CedulaUsuario = ?"
    cur.execute(sql, (CedulaUsuario,))

    Reporte = cur.fetchall()

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
            'FechaHora': row[9],
            'EvidenciaPDF': row[10]
        } for row in Reporte]


        return render_template("busqueda_historial.html", reportes= Reporte_dict)
        

    else:

        return render_template("busqueda_historial.html", mensaje= 'No se encontró ningún reporte para la cédula proporcionada.') 


############


######## Routes Instructor

# Ruta de Inicio del rol instructor 

@app.route("/inicioinstructor")
def inicioInstructor():
    return render_template("inicio_instructor.html")

# Rita para Registrar aprendiz rol instructor 

@app.route("/registrarAprendizinstructor",methods=["GET","POST"])
def registrarInstructor():
    return render_template("registrar_instructor.html", N=0)

@app.route("/registrarAprendizinstructor/<id>",methods=["GET","POST"])
def registrarInstructor2(id=0):
    return render_template("registrar_coordinacion.html", N=id)

@app.route("/registrarAprendizinstructor/i")
def registrarInstructorAprendiz():
    Identificacion=request.form.get('Identificacion')
    Nombre=request.form.get('Nombre')
    Direccion=request.form.get('Direccion')
    Telefono=request.form.get('Telefono')
    Correo=request.form.get('Correo')
    Ficha=request.form.get('Ficha')
    ProgramaFormacion=request.form.get('ProgramaFormacion')
    Rol=request.form.get('Rol')
    u1= Usuario("http://127.0.0.1:5000/registrarAprendizinstructor")
    datos={
        "Identificacion":Identificacion, "Nombre":Nombre,"Direccion":Direccion, "Telefono":Telefono, "Correo":Correo, "Ficha":Ficha, "ProgramaFormacion":ProgramaFormacion, "Rol":Rol
    }
    u1.Inserte(datos)
    id=0
    msgitos="Usuario creado satisfactoriamente" 
    print(datos)
    return render_template("alertas.html",msgitoInstructor=msgitos)

# Ruta para Reportar aprendiz rol instructor 

@app.route("/reportarAprendizinstructor/", methods=["GET, POST"])
def reportarInstructor2():
    f = requests.get("http://127.0.0.1:5000/reportarAprendizinstructor")
    fichas = f.json()
    print (f"These are the IDs: {fichas}")
    return render_template("reportar_Instructor.html", fichas=fichas)


@app.route("/reportarAprendizinstructor/" ,methods=["GET","POST"])
def reportarInstructor(id=0):
    return render_template("reportar_instructor.html", N=0)


@app.route("/reportarAprendizinstructor/i", methods = ['POST'])
def iniciarInstructor():
    Ficha=request.form.get('Ficha')
    CedulaUsuario=request.form.get('CedulaUsuario')
    Nombre=request.form.get('Nombre')
    ProgramaFormacion=request.form.get('ProgramaFormacion')
    Coordinacion=request.form.get('Coordinacion')
    TipoFalta=request.form.get('TipoFalta')
    CausasReporte=request.form.get('CausasReporte')
    Faltas=request.form.get('Faltas')
    FechaHora=request.form.get('FechaHora')
    EvidenciaPDF=request.form.get('EvidenciaPDF')
    

    u2= Usuario("http://127.0.0.1:5000/reportarAprendizinstructor")

    datos={"Ficha":Ficha, "CedulaUsuario": CedulaUsuario, "Nombre": Nombre, "ProgramaFormacion": ProgramaFormacion, "Coordinacion": Coordinacion, "TipoFalta": TipoFalta, "CausasReporte": CausasReporte, "Faltas":Faltas, "FechaHora":FechaHora, "EvidenciaPDF": EvidenciaPDF}

    u2.Inserte(datos)
    id=0
    msgitos="Reporte creado satisfactoriamente" 
    print(datos)
    return render_template("alertas.html",msgito=msgitos)

# Ruta para consultar historial del aprendiz rol instructor 

@app.route("/consultarHistorialinstructor")
def consultarInstructor():
    return render_template("consultar_instructor.html")

@app.route("/consultarHistorialinstructor/",methods=["GET","POST"])
def consultarIntructor(id=0):
    return render_template("consultar_instructor.html", N=id)

@app.route("/resultadoHistorialinstructor/")
def resultadoHistorialinstructor():
    return render_template("busqueda_instructor.html")


@app.route("/consultarHistorialinstructor/i", methods=["POST"])
def consultarAprendizinstructor():
    CedulaUsuario=request.form.get('CedulaUsuario')

    con = sqlite3.connect("./comite.db")
    cur = con.cursor()

    sql="select * from Reporte where CedulaUsuario = ?"
    cur.execute(sql, (CedulaUsuario,))

    Reporte = cur.fetchall()

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
            'FechaHora': row[9],
            'EvidenciaPDF': row[10]
        } for row in Reporte]


        return render_template("busqueda_instructor.html", reportes= Reporte_dict)
        

    else:

        msgitos="No existen reportes para este aprendiz" 
        return render_template("alertas.html",msgito=msgitos)




####### Routes Aprendiz

#Ruta inicio aprendiz 

@app.route("/inicioaprendiz")
def inicioAprendiz():
    return render_template("inicio_aprendiz.html")


#Ruta historial del aprendiz 

@app.route("/historialAprendiz")
def historialAprendiz():
    return render_template("historial_aprendiz.html")

#Ruta descargos aprendiz

@app.route("/descargosAprendiz")
def descargosAprendiz():
    return render_template("descargos_aprendiz.html")


########## Routes Relator


#Ruta acta relator 

@app.route("/actarelator")
def actaRelator():
    return render_template("acta_relator.html")

#Ruta para registrar acta (modificar)

@app.route("/registrarActa/i", methods=["POST"])
def CrearActa():
    datos = request.get_json()
    IdActa=datos['IdActa']
    FechaActa=datos['FechaActa']
    Hora=datos['Hora']
    DetallesActa=datos['DetallesActa']
    IdPlanMejora=datos['PlanMejora']

    print(f"Datos recibidos: IdActa={IdActa}, FechaActa={FechaActa}, Hora={Hora}, DetallesActa={DetallesActa}, IdPlanMejora={IdPlanMejora}")

    con = sqlite3.connect("./comite.db")
    cur = con.cursor()
    
    cur.execute("insert into Acta (IdActa, FechaActa, Hora, DetallesActa, PlanMejora) VALUES(?, ?, ?, ?, ?, ?)",IdActa, FechaActa, Hora, DetallesActa, IdPlanMejora)
    con.commit()
    con.close()
    msgitos="Acta creada satisfactoriamente" 
    return render_template("alertas.html",msgito=msgitos)
   
#Ruta para mostrar procesos relator 

@app.route("/procesosrelator")
def procesosRelator():
    return render_template("procesos_relator.html")




if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=configura['PUERTOAPP'])    
    