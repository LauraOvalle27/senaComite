from flask import Flask, jsonify,request
import json
#from services.apicnx import cnxsqlite
from database.cnxSqlite import cnxsqlite  
from config import configura 
app=Flask(__name__)
@app.route("/")
def inicio():
    return "Hola"
@app.route("/usua/cc")

@app.route("/usua/to")
def ListaUsuario():
    sql="select * from USUA" 
    con=cnxsqlite()   
    todo=con.Consultar("./usuarios.db",sql)
    return json.dumps(todo)
@app.route("/usua/<id>")
def ListaUnUsuario(id):
    sql="select * from USUA where IDUSUA="+str(id)
    con=cnxsqlite()
    todo=con.Consultar("./usuarios.db",sql)
    return json.dumps(todo)

@app.route("/usua/i",methods = ['POST'])
def CrearUsuario(): 
    datos=request.get_json()  
    ape=datos['APELLIDO']
    nom=datos['NOMBRE']
    sql="insert into USUA(NOMBRE,APELLIDO) values('"+nom+"','"+ape+"')"
    con=cnxsqlite()   
    todo=con.Ejecutar("./usuarios.db",sql)
    return "OK"
@app.route("/usua/u",methods = ['PUT'])
def EditaUsuario(): 
    datos=request.get_json()
    id=datos['IDUSUARIO']
    ape=datos['APELLIDO']
    nom=datos['NOMBRE']
    sql="update USUA set NOMBRE='"+nom+"',APELLIDO='"+ape+"' where IDUSUA="+str(id)
    con=cnxsqlite()
    todo=con.Ejecutar("./usuarios.db",sql)

    return "OK"
@app.route("/usua/d/<id>",methods = ['DELETE'])
def BorrarUsuario(id): 
    sql="delete from USUA where IDUSUA="+str(id)
    con=cnxsqlite()
    todo=con.Ejecutar("./usuarios.db",sql)
    return "OK"

if __name__=='__main__':
    app.run(debug=True,port=configura['PUERTOREST'],host='0.0.0.0')