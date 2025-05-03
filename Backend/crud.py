from sqlalchemy.orm import Session
from models import Usuarios, Pacientes, Doctores, Citas
import schemas
from schemas import UserUpdate, PatientsUpdate, DoctorsUpdate, CitasUpdate, UserLogin

def get_usuarios(db: Session):
    return db.query(Usuarios).all()

def get_usuario(db: Session, user_id: int):
    return db.query(Usuarios).filter(Usuarios.id == user_id).first()

def crear_usuario(db: Session, user: schemas.UserCreate):
    db_usuario = Usuarios(**user.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def actualizar_usuario(db: Session, user_id: int, user: UserUpdate):
    db_usuario = db.query(Usuarios).filter(Usuarios.id == user_id).first()
    if db_usuario:
        db_usuario.nombre = user.nombre
        db_usuario.username = user.username
        if user.password:
            db_usuario.password = user.password
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def eliminar_usuario(db: Session, user_id: int):
    db_usuario = db.query(Usuarios).filter(Usuarios.id == user_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario

#PACIENTES
def get_pacientes(db: Session):
    return db.query(Pacientes).all()

def get_paciente(db: Session, paciente_id: int):
    return db.query(Pacientes).filter(Pacientes.id == paciente_id).first()

def crear_paciente(db: Session, paciente: schemas.PatientsCreate):
    db_paciente = Pacientes(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def actualizar_paciente(db: Session, paciente_id: int, paciente: PatientsUpdate):
    db_paciente = db.query(Pacientes).filter(Pacientes.id == paciente_id).first()
    if db_paciente:
        db_paciente.nombre = paciente.nombre
        db_paciente.identificacion = paciente.identificacion
        db_paciente.sexo = paciente.sexo
        db_paciente.edad = paciente.edad
        db_paciente.correo = paciente.correo
        db_paciente.telefono = paciente.telefono
        
        db.commit()
        db.refresh(db_paciente)
    return db_paciente

def eliminar_paciente(db: Session, paciente_id: int):
    db_paciente = db.query(Pacientes).filter(Pacientes.id == paciente_id).first()
    if db_paciente:
        db.delete(db_paciente)
        db.commit()
    return db_paciente
#FIN PACIENTES

#DOCTORES
def get_doctores(db: Session):
    return db.query(Doctores).all()

def get_doctor(db: Session, doctor_id: int):
    return db.query(Doctores).filter(Doctores.id == doctor_id).first()

def crear_doctor(db: Session, doctor: schemas.PatientsCreate):
    db_doctor = Doctores(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def actualizar_doctor(db: Session, doctor_id: int, doctor: PatientsUpdate):
    db_doctor = db.query(Doctores).filter(Doctores.id == doctor_id).first()
    if db_doctor:
        db_doctor.nombre = doctor.nombre
        db_doctor.identificacion = doctor.identificacion
        db_doctor.especialidad = doctor.especialidad
        db_doctor.correo = doctor.correo
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

def eliminar_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(Doctores).filter(Doctores.id == doctor_id).first()
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return db_doctor
#FIN DOCTORES

# CITAS
def get_citas(db: Session):
    return db.query(Citas).all()

def get_cita(db: Session, cita_id: int):
    return db.query(Citas).filter(Citas.id == cita_id).first()

def crear_cita(db: Session, cita: schemas.CitasCreate):
    db_cita = Citas(**cita.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def actualizar_cita(db: Session, cita_id: int, cita: schemas.CitasUpdate):
    db_cita = db.query(Citas).filter(Citas.id == cita_id).first()
    if db_cita:
        db_cita.paciente_id = cita.paciente_id
        db_cita.doctor_id = cita.doctor_id
        db_cita.fecha = cita.fecha
        db_cita.hora = cita.hora
        db_cita.estado = cita.estado
        db_cita.observaciones = cita.observaciones
        db.commit()
        db.refresh(db_cita)
    return db_cita

def eliminar_cita(db: Session, cita_id: int):
    db_cita = db.query(Citas).filter(Citas.id == cita_id).first()
    if db_cita:
        db.delete(db_cita)
        db.commit()
    return db_cita
# FIN CITAS


#LOGIN
def login_user(db: Session, username: str, password: str):
    usuario = db.query(Usuarios).filter(Usuarios.username == username, Usuarios.password == password).first()
    return usuario

