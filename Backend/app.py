from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud, models, schemas
from models import Base
from crud import get_usuarios, crear_usuario, actualizar_usuario

#Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/usuarios", tags=["Usuarios"])
def listado_Usuarios(db: Session = Depends(get_db)):
    users = get_usuarios(db=db)
    return users

@app.get("/usuarios/{user_id}", response_model=schemas.UserBase, tags=["Usuarios"])
def Usuario_Id(user_id: int, db: Session = Depends(get_db)):
    users = crud.get_usuario(db=db, user_id=user_id)
    if users is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return users

@app.post("/usuarios", response_model=schemas.UserCreate, tags=["Usuarios"])
def Crear_Usuario(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db=db, user=user)

@app.put("/usuarios/{user_id}", response_model=schemas.UserBase, tags=["Usuarios"])
def Actualizar_Usuario(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    users = crud.actualizar_usuario(db=db, user_id=user_id, user=user)
    if users is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return users

@app.delete("/usuarios/{user_id}", response_model=schemas.UserBase, tags=["Usuarios"])
def Eliminar_Usuario(user_id: int, db: Session = Depends(get_db)):
    users = crud.eliminar_usuario(db=db, user_id=user_id)
    if users is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return users

#PACIENTES CRUD
@app.get("/pacientes", tags=["Pacientes"])
def listado_pacientes(db: Session = Depends(get_db)):
    pacientes = crud.get_pacientes(db=db)
    return pacientes

@app.get("/pacientes/{paciente_id}", response_model=schemas.PatientsBase, tags=["Pacientes"])
def paciente_id(paciente_id: int, db: Session = Depends(get_db)):
    paciente = crud.get_paciente(db=db, paciente_id=paciente_id)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@app.post("/pacientes", response_model=schemas.PatientsCreate, tags=["Pacientes"])
def crear_paciente(paciente: schemas.PatientsCreate, db: Session = Depends(get_db)):
    return crud.crear_paciente(db=db, paciente=paciente)

@app.put("/pacientes/{paciente_id}", response_model=schemas.PatientsBase, tags=["Pacientes"])
def actualizar_paciente(paciente_id: int, paciente: schemas.PatientsUpdate, db: Session = Depends(get_db)):
    paciente_actualizado = crud.actualizar_paciente(db=db, paciente_id=paciente_id, paciente=paciente)
    if paciente_actualizado is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente_actualizado

@app.delete("/pacientes/{paciente_id}", response_model=schemas.PatientsBase, tags=["Pacientes"])
def eliminar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = crud.eliminar_paciente(db=db, paciente_id=paciente_id)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

#FIN PACIENTE CRUD

#DOCTORES CRUD
@app.get("/doctores", tags=["Doctores"])
def listado_doctores(db: Session = Depends(get_db)):
    doctores = crud.get_doctores(db=db)
    return doctores

@app.get("/doctores/{doctor_id}", response_model=schemas.DoctorsBase, tags=["Doctores"])
def doctor_id(doctor_id: int, db: Session = Depends(get_db)):
    doctor = crud.get_doctor(db=db, doctor_id=doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctores no encontrado")
    return doctor

@app.post("/doctores", response_model=schemas.DoctorsCreate, tags=["Doctores"])
def crear_doctor(doctor: schemas.DoctorsCreate, db: Session = Depends(get_db)):
    return crud.crear_doctor(db=db, doctor=doctor)

@app.put("/doctores/{doctor_id}", response_model=schemas.DoctorsBase, tags=["Doctores"])
def actualizar_doctor(doctor_id: int, doctor: schemas.DoctorsUpdate, db: Session = Depends(get_db)):
    doctor_actualizado = crud.actualizar_doctor(db=db, doctor_id=doctor_id, doctor=doctor)
    if doctor_actualizado is None:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor_actualizado

@app.delete("/doctores/{doctor_id}", response_model=schemas.DoctorsBase, tags=["Doctores"])
def eliminar_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = crud.eliminar_doctor(db=db, doctor_id=doctor_id)
    if doctor is None:
        raise HTTPException(status_code=404, detail="doctor no encontrado")
    return doctor
#FIN PACIENTE CRUD

#CITAS CRUD
@app.get("/citas", tags=["Citas"])
def listado_citas(db: Session = Depends(get_db)):
    citas = crud.get_citas(db=db)
    return citas

@app.get("/citas/{cita_id}", response_model=schemas.CitasBase, tags=["Citas"])
def obtener_cita(cita_id: int, db: Session = Depends(get_db)):
    cita = crud.get_cita(db=db, cita_id=cita_id)
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@app.post("/citas", response_model=schemas.CitasCreate, tags=["Citas"])
def crear_cita(cita: schemas.CitasCreate, db: Session = Depends(get_db)):
    return crud.crear_cita(db=db, cita=cita)

@app.put("/citas/{cita_id}", response_model=schemas.CitasBase, tags=["Citas"])
def actualizar_cita(cita_id: int, cita: schemas.CitasUpdate, db: Session = Depends(get_db)):
    cita_actualizada = crud.actualizar_cita(db=db, cita_id=cita_id, cita=cita)
    if cita_actualizada is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita_actualizada

@app.delete("/citas/{cita_id}", response_model=schemas.CitasBase, tags=["Citas"])
def eliminar_cita(cita_id: int, db: Session = Depends(get_db)):
    cita = crud.eliminar_cita(db=db, cita_id=cita_id)
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita
#FIN CITAS CRIUD

#LOGIN
@app.post("/login", tags=["Login"])
def login(u: schemas.UserLogin, db: Session = Depends(get_db)):
    usuario = crud.login_user(db, u.username, u.password)
    if usuario:
        return {"message": "Credenciales correctas"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")