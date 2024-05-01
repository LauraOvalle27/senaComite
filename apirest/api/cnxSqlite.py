import sqlite3
class cnxsqlite:
    def Consultar(self,bd,sql):
        con = sqlite3.connect(bd)
        cur = con.cursor()
        res=cur.execute(sql)
        todo=res.fetchall()
        con.close() 
        return todo   
    def ConsultarUno(self,bd,sql):
        con = sqlite3.connect(bd)
        todo={}
        cur = con.cursor()
        res=cur.execute(sql)
        nombres_columnas = [str(descripcion[0]) for descripcion in cur.description]
        primer_resultado = res.fetchone()
        for i,valor in enumerate(primer_resultado):
            nombrecol=nombres_columnas[i]
            todo[nombrecol]=valor
        con.close() 
        return todo  
    def ConsultarJson(self,bd,sql):
        con = sqlite3.connect(bd)
        todo={}
        cur = con.cursor()
        res=cur.execute(sql)
        nombres_columnas = [str(descripcion[0]) for descripcion in cur.description]
        primer_resultado = res.fetchall()
        for i,valor in enumerate(primer_resultado):
            nombrecol=nombres_columnas[i]
            todo[nombrecol]=valor
        con.close() 
        return todo  
    def Ejecutar(self,bd,sql):
        con = sqlite3.connect(bd)
        cur = con.cursor()
        res=cur.execute(sql)
        con.commit()
        con.close()