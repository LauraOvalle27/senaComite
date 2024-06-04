import sqlite3 as sql

def bd():
    conn = sql.connect("comite.db")
    cur = conn.cursor()
    script = """
    PRAGMA foreign_keys = ON;

    CREATE TABLE Usuario (
        Identificacion INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL,
        ProgramaFormacion TEXT NOT NULL,
        Ficha INTEGER NOT NULL,
        Direccion TEXT NOT NULL,
        Telefono INTEGER NOT NULL,
        Correo TEXT NOT NULL,
        Rol INTEGER NOT NULL
    );

    CREATE INDEX idx_correo ON Usuario (Correo);

    CREATE TABLE Reporte(
        IdReporte INTEGER PRIMARY KEY,
        CedulaUsuario INTEGER NOT NULL,
        Nombre TEXT NOT NULL,
        Ficha INTEGER NOT NULL,
        ProgramaFormacion TEXT NOT NULL,
        Coordinacion TEXT NOT NULL,
        TipoFalta TEXT NOT NULL,
        CausasReporte TEXT NOT NULL, 
        Faltas INTEGER NOT NULL,
        EvidenciaPDF TEXT NOT NULL, 
        FOREIGN KEY(CedulaUsuario) REFERENCES Usuario (Identificacion)
    );

    CREATE TABLE Proceso (
        IdProceso INTEGER PRIMARY KEY AUTOINCREMENT,
        FechaCitacion DATE NOT NULL,
        Descargos TEXT NOT NULL,
        Decision TEXT NOT NULL,
        Estado INTEGER NOT NULL,
        Motivo TEXT NOT NULL,
        Resumen TEXT NOT NULL,
        Evidencias TEXT NOT NULL, 
        IdReporte INTEGER NOT NULL,
        FOREIGN KEY (IdReporte) REFERENCES Reporte (IdReporte)
    );

    CREATE TABLE planMejora(
        IdPlanMejora INTEGER PRIMARY KEY NOT NULL,
        Situacion TEXT NOT NULL,
        FechaInicio DATE NOT NULL, 
        FechaLimite DATE NOT NULL,
        IdInstructor INTEGER,
        EvidenciaPDF TEXT NOT NULL, 
        FOREIGN KEY (IdInstructor) REFERENCES Usuario (Identificacion)
    );

    CREATE TABLE Acta (
        IdActa INTEGER PRIMARY KEY,
        FechaActa DATE NOT NULL,
        Hora TIME NOT NULL,
        DetallesActa TEXT NOT NULL, 
        IdPlanMejora INTEGER NOT NULL,
        FOREIGN KEY (IdPlanMejora) REFERENCES planMejora (IdPlanMejora)
    );

    CREATE TABLE Generar(
        IdProceso INTEGER NOT NULL,
        IdPlanMejora INTEGER NOT NULL,
        FOREIGN KEY (IdProceso) REFERENCES Proceso(IdProceso),
        FOREIGN KEY (IdPlanMejora) REFERENCES planMejora(IdPlanMejora)
    );

    CREATE TABLE Citacion(
        IdProceso INTEGER NOT NULL,
        IdComite INTEGER NOT NULL,
        Correo TEXT NOT NULL,
        FOREIGN KEY (IdProceso) REFERENCES Proceso(IdProceso),
        FOREIGN KEY (IdComite) REFERENCES Usuario(Identificacion),
        FOREIGN KEY (Correo) REFERENCES Usuario(Correo)
    );

    INSERT INTO Usuario (Identificacion, Nombre, ProgramaFormacion, Correo, Ficha, Telefono, Direccion, Rol) 
    VALUES (10468594, 'Miguel', 'ADSO', 'miguel@gmail.com', 451230, 233456, 'carrera 45 #85', 1);

    INSERT INTO Reporte (IdReporte, Ficha, CedulaUsuario, Nombre, ProgramaFormacion, Coordinacion, TipoFalta, CausasReporte, Faltas, EvidenciaPDF) 
    VALUES (1, 1423647, 10468594, 'juanito pablo', 'adso', 'logistica', 'grave', 'El joven fomenta el desorden', 'Contribuir al desaseo', 'hello.PDF');
    """
    cur.executescript(script)
    conn.commit()

    # Fetch and display data from the tables
    cur.execute("SELECT * FROM Usuario;")
    usuarios = cur.fetchall()
    print("Usuarios:", usuarios)

    cur.execute("SELECT * FROM Proceso;")
    procesos = cur.fetchall()
    print("Procesos:", procesos)

    cur.execute("SELECT * FROM Reporte;")
    reportes = cur.fetchall()
    print("Reportes:", reportes)

    cur.execute("SELECT * FROM planMejora;")
    planes = cur.fetchall()
    print("Planes de Mejora:", planes)

    cur.execute("SELECT * FROM Acta;")
    actas = cur.fetchall()
    print("Actas:", actas)

    cur.execute("SELECT * FROM Generar;")
    generar = cur.fetchall()
    print("Generar:", generar)

    cur.execute("SELECT * FROM Citacion;")
    citaciones = cur.fetchall()
    print("Citaciones:", citaciones)

    conn.close()

if __name__ == "__main__":
    bd()
