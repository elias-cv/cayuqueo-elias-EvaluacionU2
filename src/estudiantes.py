from sqlalchemy import select
from conexion import Session
from modelos import Estudiantes


def registrar_estudiante(nombre: str, correo: str):
    if not nombre or not correo:
        raise ValueError("El nombre y el correo son obligatorios.")
    with Session.begin() as session:
        estudiante_existente = session.scalar(
            select(Estudiantes).where(Estudiantes.correo == correo)
        )
        if estudiante_existente:
            raise ValueError(f"El correo {correo} ya está registrado para otro estudiante.")
        nuevo_estudiante = Estudiantes(nombre=nombre, correo=correo)
        session.add(nuevo_estudiante)
        return nuevo_estudiante


def listar_estudiantes():
    with Session() as session:
        return session.scalars(select(Estudiantes)).all()


def buscar_estudiante_id(id_estudiante: int):
    with Session() as session:
        estudiante = session.get(Estudiantes, id_estudiante)
        if estudiante is None:
            raise ValueError("Estudiante no encontrado")
        return estudiante