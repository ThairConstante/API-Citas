from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time, Text
from database import Base

class Usuarios(Base):
    __tablename__= "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)


class Pacientes(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    identificacion = Column(String, unique=True, index=True)
    sexo = Column(String, unique=True, index=True)
    edad = Column(String, unique=True, index=True)
    correo = Column(String, unique=True, index=True)
    telefono = Column(String, unique=True, index=True)


class Doctores(Base):
    __tablename__ = "doctores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    identificacion = Column(String, unique=True, index=True)
    especialidad = Column(String, unique=True, index=True)
    correo = Column(String, unique=True, index=True)

class Citas(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctores.id"), nullable=False) 
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    estado = Column(Integer, nullable=False)
    observaciones = Column(Text, nullable=True)
