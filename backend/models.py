from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Conexión a la base de datos (archivo local SQLite)
DATABASE_URL = "sqlite:///mantenimiento.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()


class Maquina(Base):
    __tablename__ = "maquinas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String)
    ubicacion_planta = Column(String)
    manual_url = Column(String, nullable=True)

    repuestos = relationship("Repuesto", back_populates="maquina")
    eventos = relationship("Evento", back_populates="maquina")


class Repuesto(Base):
    __tablename__ = "repuestos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    maquina_id = Column(Integer, ForeignKey("maquinas.id"))
    ubicacion_almacen = Column(String)
    stock_actual = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)

    maquina = relationship("Maquina", back_populates="repuestos")


class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    maquina_id = Column(Integer, ForeignKey("maquinas.id"))
    usuario = Column(String, nullable=False)
    tipo = Column(String)  # averia, mantenimiento, comentario_turno
    turno = Column(String)  # mañana, tarde, noche
    fecha_hora = Column(DateTime)
    descripcion = Column(String)
    resuelto = Column(Boolean, default=False)

    maquina = relationship("Maquina", back_populates="eventos")


def crear_tablas():
    Base.metadata.create_all(bind=engine)