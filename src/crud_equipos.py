from sqlalchemy import select
from conexion import Session
from modelos import Equipo


def crear_equipo(nombre: str, tipo: str, stock_disponible: int):
    if not nombre or not tipo:
        raise ValueError("El nombre y el tipo son obligatorios.")
    if stock_disponible < 0:
        raise ValueError("El stock disponible no puede ser negativo.")
    with Session.begin() as session:
        nuevo_equipo = Equipo(nombre=nombre, tipo=tipo, stock_disponible=stock_disponible)
        session.add(nuevo_equipo)
        return nuevo_equipo


def listar_equipos():
    with Session() as session:
        return session.scalars(select(Equipo)).all()


def buscar_equipo_id(id_equipo: int):
    with Session() as session:
        equipo = session.get(Equipo, id_equipo)
        if equipo is None:
            raise ValueError("Equipo no encontrado")
        return equipo


def actualizar_equipo(id_equipo: int, nombre: str = None, tipo: str = None, stock_disponible: int = None):
    with Session.begin() as session:
        equipo = session.get(Equipo, id_equipo)
        if equipo is None:
            raise ValueError("Equipo no encontrado")
        if nombre is not None:
            equipo.nombre = nombre
        if tipo is not None:
            equipo.tipo = tipo
        if stock_disponible is not None:
            if stock_disponible < 0:
                raise ValueError("El stock disponible no puede ser negativo.")
            equipo.stock_disponible = stock_disponible
        return equipo


def eliminar_equipo(id_equipo: int):
    with Session.begin() as session:
        equipo = session.get(Equipo, id_equipo)
        if equipo is None:
            raise ValueError("Equipo no encontrado")
        session.stock_disponible -= equipo.stock_disponible
        session.delete(equipo)
        return True
