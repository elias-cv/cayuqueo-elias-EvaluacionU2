from sqlalchemy import select
from sqlalchemy.orm import selectinload
from conexion import Session
from modelos import Prestamos, Equipo, Estudiantes
from datetime import datetime


def crear_prestamo(equipo_id: int, estudiante_id: int, cantidad: int):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")
    with Session.begin() as session:
        equipo = session.get(Equipo, equipo_id)
        estudiante = session.get(Estudiantes, estudiante_id)
        if not equipo:
            raise ValueError(f"Equipo con ID {equipo_id} no encontrado.")
        if not estudiante:
            raise ValueError(f"Estudiante con ID {estudiante_id} no encontrado.")
        if equipo.stock_disponible < cantidad:
            raise ValueError(f"No hay suficiente stock disponible para el equipo {equipo.nombre}.")
        prestamo = Prestamos(
            fecha=datetime.now(),
            cantidad=cantidad,
            estado=True,
            equipo=equipo,
            estudiante=estudiante,
        )
        equipo.stock_disponible -= cantidad
        session.add(prestamo)
        return prestamo


def listar_prestamos():
    with Session() as session:
        return session.scalars(
            select(Prestamos)
            .options(
                selectinload(Prestamos.equipo),
                selectinload(Prestamos.estudiante),
            )
        ).all()


def devolver_prestamo(prestamo_id: int):
    with Session.begin() as session:
        prestamo = session.get(Prestamos, prestamo_id)
        if not prestamo:
            raise ValueError(f"Préstamo con ID {prestamo_id} no encontrado.")
        if prestamo.estado is False:
            raise ValueError(f"El préstamo con ID {prestamo_id} ya ha sido devuelto.")
        prestamo.estado = False
        prestamo.equipo.stock_disponible += prestamo.cantidad
        return prestamo