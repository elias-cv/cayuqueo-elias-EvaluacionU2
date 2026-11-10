from conexion import engine
from modelos import Base

def crear_tablas():
    Base.metadata.create_all(engine)
    print("Tablas de Equipo, Estudiantes y Prestamos creadas correctamente")

if __name__ == "__main__":
    crear_tablas()