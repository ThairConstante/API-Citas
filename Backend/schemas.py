from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class UserBase(BaseModel):
    id: int
    nombre: str
    username: str
    password: str

class UserCreate(BaseModel):
    nombre: str
    username: str
    password: str

class UserUpdate(BaseModel):
    nombre: str
    username: str
    password: Optional[str] = None

#PACIENTES
class PatientsBase(BaseModel):
    id: int
    nombre: str
    identificacion: str
    sexo: str
    edad: str
    correo: str
    telefono: str

class PatientsCreate(BaseModel):
    nombre: str
    identificacion: str
    sexo: str
    edad: str
    correo: str
    telefono: str

class PatientsUpdate(BaseModel):
    nombre: str
    identificacion: str
    sexo: str
    edad: str
    correo: str
    telefono: str
#FIN PACIENTES

#DOCTORES
class DoctorsBase(BaseModel):
    id: int
    nombre: str
    identificacion: str
    especialidad: str
    correo: str

class DoctorsCreate(BaseModel):
    nombre: str
    identificacion: str
    especialidad: str
    correo: str

class DoctorsUpdate(BaseModel):
    nombre: str
    identificacion: str
    especialidad: str
    correo: str
#FIN DOCTORES

#CITAS
class CitasBase(BaseModel):
    id: int
    paciente_id: int
    doctor_id: int
    fecha: date
    hora: time
    estado: int
    observaciones: Optional[str] = None

class CitasCreate(BaseModel):
    paciente_id: int
    doctor_id: int
    fecha: date
    hora: time
    estado: int
    observaciones: Optional[str] = None

class CitasUpdate(BaseModel):
    paciente_id: int
    doctor_id: int
    fecha: date
    hora: time
    estado: int
    observaciones: Optional[str] = None
#FIN CITAS

#LOGIN
class UserLogin(BaseModel):
    username: str
    password: str
