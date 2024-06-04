import sqlite3
from flask import Flask, jsonify,request,redirect, url_for
import json,requests
from flask import render_template
from services.apicnx import Usuario   
from config import configura    

app=Flask(__name__)

########## inicio


@app.route('/')
def index():
    return redirect (url_for("loginUsuarios"))

@app.route('/login')
def loginUsuarios():
    return render_template ("login.html")


@app.route('/iniciocoordinacion')
def incioCoordinacion():
    return render_template("inicio_coordinacion.html")

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


@app.route("/reportarAprendizcoordinacion/" ,methods=["GET","POST"])
def reportarCoordinacion():
    return render_template("reportar_coordinacion.html", N=0)

@app.route("/reportarAprendizcoordinacion/" ,methods=["GET","POST"])
def reportarCoordinacion2(id=0):
    return render_template("reportar_coordinacion.html", N=id)

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
    EvidenciaPDF=request.form.get('EvidenciaPDF')
    

    u2= Usuario("http://127.0.0.1:5000/reportarAprendizcoordinacion")

    datos={"Ficha":Ficha, "CedulaUsuario": CedulaUsuario, "Nombre": Nombre, "ProgramaFormacion": ProgramaFormacion, "Coordinacion": Coordinacion, "TipoFalta": TipoFalta, "CausasReporte": CausasReporte, "Faltas":Faltas, "EvidenciaPDF": EvidenciaPDF}

    u2.Inserte(datos)
    id=0
    msgitos="Reporte creado satisfactoriamente" 
    print(datos)
    return render_template("alertas.html",msgito=msgitos)



@app.route("/procesosPendientescoordinacion")
def procesosPendientes():
    return render_template("procesos_coordinacion.html")

@app.route("/citacioncoordinacion")
def citacion():
    return render_template("citacion_coordinacion.html")




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
            'EvidenciaPDF': row[9]
        } for row in Reporte]


        return render_template("busqueda_historial.html", reportes= Reporte_dict)
        

    else:

        return render_template("busqueda_historial.html", mensaje= 'No se encontró ningún reporte para la cédula proporcionada.') 





@app.route("/inicioinstructor")
def inicioInstructor():
    return render_template("inicio_instructor.html")

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



@app.route("/reportarAprendizinstructor/" ,methods=["GET","POST"])
def reportarInstructor():
    return render_template("reportar_instructor.html", N=0)

@app.route("/reportarAprendizcoordinacion/" ,methods=["GET","POST"])
def reportarInstructor2(id=0):
    return render_template("reportar_instructor.html", N=id)

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
    EvidenciaPDF=request.form.get('EvidenciaPDF')
    

    u2= Usuario("http://127.0.0.1:5000/reportarAprendizinstructor")

    datos={"Ficha":Ficha, "CedulaUsuario": CedulaUsuario, "Nombre": Nombre, "ProgramaFormacion": ProgramaFormacion, "Coordinacion": Coordinacion, "TipoFalta": TipoFalta, "CausasReporte": CausasReporte, "Faltas":Faltas, "EvidenciaPDF": EvidenciaPDF}

    u2.Inserte(datos)
    id=0
    msgitos="Reporte creado satisfactoriamente" 
    print(datos)
    return render_template("alertas.html",msgito=msgitos)

@app.route("/consultarHistorialinstructor")
def consultarInstructor():
    return render_template("consultar_instructor.html")
@app.route("/consultarHistorialinstructor/",methods=["GET","POST"])
def consultarIntructor(id=0):
    return render_template("consultar_coordinacion.html", N=id)
@app.route("/resultadoHistorialinstructor/")
def resultadoHistorialinstructor():
    return render_template("busqueda_historial.html")


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
            'EvidenciaPDF': row[9]
        } for row in Reporte]


        return render_template("busqueda_historial.html", reportes= Reporte_dict)
        

    else:

        msgitos="No existen reportes para este aprendiz" 
        return render_template("alertas.html",msgito=msgitos)



@app.route("/inicioaprendiz")
def inicioAprendiz():
    return render_template("inicio_aprendiz.html")

@app.route("/historialAprendiz")
def historialAprendiz():
    return render_template("historial_aprendiz.html")

@app.route("/descargosAprendiz")
def descargosAprendiz():
    return render_template("descargos_aprendiz.html")

@app.route("/actarelator")
def actaRelator():
    return render_template("acta_relator.html")

@app.route("/procesosrelator")
def procesosRelator():
    return render_template("procesos_relator.html")





if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=configura['PUERTOAPP'])    
    