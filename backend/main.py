from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas
from database import get_db

from datetime import date

app = FastAPI(title="Smart Maintenance QR API")


@app.get("/")
def read_root():
    return {"mensaje": "API de Smart Maintenance QR funcionando correctamente"}


# ---------- MÁQUINAS ----------

@app.post("/maquinas", response_model=schemas.MaquinaResponse)
def crear_maquina(maquina: schemas.MaquinaCreate, db: Session = Depends(get_db)):
    nueva_maquina = models.Maquina(**maquina.model_dump())
    db.add(nueva_maquina)
    db.commit()
    db.refresh(nueva_maquina)
    return nueva_maquina


@app.get("/maquinas", response_model=list[schemas.MaquinaResponse])
def listar_maquinas(db: Session = Depends(get_db)):
    return db.query(models.Maquina).all()


@app.get("/maquinas/{maquina_id}", response_model=schemas.MaquinaResponse)
def obtener_maquina(maquina_id: int, db: Session = Depends(get_db)):
    maquina = db.query(models.Maquina).filter(models.Maquina.id == maquina_id).first()
    if not maquina:
        raise HTTPException(status_code=404, detail="Máquina no encontrada")
    return maquina


# ---------- EVENTOS ----------

@app.post("/eventos", response_model=schemas.EventoResponse)
def crear_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    nuevo_evento = models.Evento(**evento.model_dump(), fecha_hora=datetime.now())
    db.add(nuevo_evento)
    db.commit()
    db.refresh(nuevo_evento)
    return nuevo_evento


@app.get("/eventos", response_model=list[schemas.EventoResponse])
def listar_eventos(db: Session = Depends(get_db)):
    return db.query(models.Evento).order_by(models.Evento.fecha_hora.desc()).all()


@app.get("/maquinas/{maquina_id}/eventos", response_model=list[schemas.EventoResponse])
def eventos_de_maquina(maquina_id: int, db: Session = Depends(get_db)):
    return db.query(models.Evento).filter(models.Evento.maquina_id == maquina_id).all()




# ---------- CUADERNO DE TURNO ----------

@app.get("/cuaderno-turno", response_model=list[schemas.EventoResponse])
def cuaderno_turno(
    turno: str | None = None,
    fecha: date | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Evento)

    if turno:
        query = query.filter(models.Evento.turno == turno)

    if fecha:
        query = query.filter(
            models.Evento.fecha_hora >= datetime.combine(fecha, datetime.min.time()),
            models.Evento.fecha_hora < datetime.combine(fecha, datetime.max.time())
        )

    return query.order_by(models.Evento.fecha_hora.desc()).all()

# ---------- REPUESTOS ----------

@app.post("/repuestos", response_model=schemas.RepuestoResponse)
def crear_repuesto(repuesto: schemas.RepuestoCreate, db: Session = Depends(get_db)):
    nuevo_repuesto = models.Repuesto(**repuesto.model_dump())
    db.add(nuevo_repuesto)
    db.commit()
    db.refresh(nuevo_repuesto)
    return nuevo_repuesto

@app.get("/repuestos", response_model=list[schemas.RepuestoResponse])
def listar_repuestos(db: Session = Depends(get_db)):
    return db.query(models.Repuesto).all()


@app.get("/maquinas/{maquina_id}/repuestos", response_model=list[schemas.RepuestoResponse])
def repuestos_de_maquina(maquina_id: int, db: Session = Depends(get_db)):
    return db.query(models.Repuesto).filter(models.Repuesto.maquina_id == maquina_id).all()

@app.patch("/repuestos/{repuesto_id}/stock", response_model=schemas.RepuestoResponse)
def actualizar_stock(repuesto_id: int, datos: schemas.RepuestoStockUpdate, db: Session = Depends(get_db)):
    repuesto = db.query(models.Repuesto).filter(models.Repuesto.id == repuesto_id).first()
    if not repuesto:
        raise HTTPException(status_code=404, detail="Repuesto no encontrado")

    repuesto.stock_actual = datos.stock_actual
    db.commit()
    db.refresh(repuesto)
    return repuesto