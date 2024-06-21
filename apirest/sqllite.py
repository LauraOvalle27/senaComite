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
        FechaHora DATETIME NOT NULL,
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
        Identificacion INTEGER NOT NULL,
        FOREIGN KEY (IdProceso) REFERENCES Proceso(IdProceso),
        FOREIGN KEY (Identificacion) REFERENCES Usuario(Identificacion)
    
    );

    INSERT INTO Usuario (Identificacion, Nombre, ProgramaFormacion, Correo, Ficha, Telefono, Direccion, Rol) 
    VALUES (10468595, 'Ana', 'ADSO', 'ana@gmail.com', 451231, 233457, 'calle 12 #34', 2),
           (10468596, 'Carlos', 'ADSO', 'carlos@gmail.com', 451232, 233458, 'avenida 9 #10', 1),
           (10468597, 'Laura', 'ADSO', 'laura@gmail.com', 451233, 233459, 'carrera 7 #8', 2),
           (10468598, 'Jorge', 'ADSO', 'jorge@gmail.com', 451234, 233460, 'carrera 3 #6', 1),
           (10468599, 'Sofia', 'ADSO', 'sofia@gmail.com', 451235, 233461, 'calle 45 #78', 2);


    
    INSERT INTO Reporte (IdReporte, Ficha, CedulaUsuario, Nombre, ProgramaFormacion, Coordinacion, TipoFalta, CausasReporte, Faltas, FechaHora, EvidenciaPDF) 
    VALUES (1, 451231, 10468595, 'Ana', 'ADSO', 'logistica', 'grave', 'El joven fomenta el desorden', 'Contribuir al desaseo', '04/06/2024 3:34', 'hello.PDF');
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
