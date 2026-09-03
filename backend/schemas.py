from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MaquinaCreate(BaseModel):
    nombre: str
    tipo: Optional[str] = None
    ubicacion_planta: Optional[str] = None
    manual_url: Optional[str] = None


class MaquinaResponse(MaquinaCreate):
    id: int

    class Config:
        from_attributes = True


class EventoCreate(BaseModel):
    maquina_id: int
    usuario: str
    tipo: str
    turno: str
    descripcion: str


class EventoResponse(EventoCreate):
    id: int
    fecha_hora: datetime
    resuelto: bool

    class Config:
        from_attributes = True

class RepuestoCreate(BaseModel):
    nombre: str
    maquina_id: int
    ubicacion_almacen: Optional[str] = None
    stock_actual: int = 0
    stock_minimo: int = 0


class RepuestoResponse(RepuestoCreate):
    id: int

    class Config:
        from_attributes = True

class RepuestoStockUpdate(BaseModel):
    stock_actual: int