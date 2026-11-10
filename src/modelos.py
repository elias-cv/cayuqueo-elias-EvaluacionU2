from sqlalchemy import String, Integer, Boolean, ForeignKey, CheckConstraint, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Equipo(Base):
    __tablename__ = 'equipos'
    __tableargs__ = (
        CheckConstraint('stock_disponible >= 0', name='check_stock_disponible'),
    )
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False)
    stock_disponible: Mapped[int] = mapped_column(Integer, nullable=False)
    prestamos: Mapped[list["Prestamos"]] = relationship("Prestamos", back_populates="equipo")

class Estudiantes(Base):
    __tablename__ = 'estudiantes'
    id: Mapped[int] = mapped_column(Integer,  primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    prestamos: Mapped[list["Prestamos"]] = relationship("Prestamos", back_populates="estudiante")

class Prestamos(Base):
    __tablename__ = 'prestamos'
    __tableargs__ = (
        CheckConstraint('fecha >= CURRENT_TIMESTAMP', name='check_fecha'),
        CheckConstraint('cantidad > 0', name='check_cantidad')
    )
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fecha: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    estado: Mapped[bool] = mapped_column(Boolean, nullable=False)
    equipo_id: Mapped[int] = mapped_column(ForeignKey('equipos.id'))
    estudiante_id: Mapped[int] = mapped_column(ForeignKey('estudiantes.id'))
    equipo: Mapped["Equipo"] = relationship("Equipo", back_populates="prestamos")
    estudiante: Mapped["Estudiantes"] = relationship("Estudiantes", back_populates="prestamos")
