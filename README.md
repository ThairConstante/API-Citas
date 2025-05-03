# **API de Asignación de Citas Médicas**

## **Descripción**

Este proyecto es un sistema completo para la gestión de citas médicas, compuesto por una API RESTful desarrollada con FastAPI y un frontend ya implementado. Permite registrar usuarios, pacientes y doctores, y gestionar la asignación de citas mediante operaciones CRUD. Incluye autenticación básica y soporte CORS para facilitar la conexión con la interfaz web.

## **Tecnologías Usadas**

### Backend
- **FastAPI** – Framework para construir la API RESTful.
- **SQLAlchemy** – ORM para interactuar con la base de datos.
- **Pydantic** – Validación de datos.
- **Uvicorn** – Servidor ASGI para ejecutar la aplicación.
- **CORS Middleware** – Para permitir la comunicación con el frontend.

### Frontend
- **HTML, CSS y JavaScript**
- **Axios** – Para consumir la API.

## **Endpoints**

### **Usuarios**
- **GET** `/usuarios`: Lista todos los usuarios.
- **GET** `/usuarios/{user_id}`: Detalles de un usuario por ID.
- **POST** `/usuarios`: Crear un nuevo usuario.
- **PUT** `/usuarios/{user_id}`: Actualizar usuario por ID.
- **DELETE** `/usuarios/{user_id}`: Eliminar usuario por ID.

### **Pacientes**
- **GET** `/pacientes`: Lista todos los pacientes.
- **GET** `/pacientes/{paciente_id}`: Detalles de un paciente por ID.
- **POST** `/pacientes`: Crear un nuevo paciente.
- **PUT** `/pacientes/{paciente_id}`: Actualizar paciente por ID.
- **DELETE** `/pacientes/{paciente_id}`: Eliminar paciente por ID.

### **Doctores**
- **GET** `/doctores`: Lista todos los doctores.
- **GET** `/doctores/{doctor_id}`: Detalles de un doctor por ID.
- **POST** `/doctores`: Crear un nuevo doctor.
- **PUT** `/doctores/{doctor_id}`: Actualizar doctor por ID.
- **DELETE** `/doctores/{doctor_id}`: Eliminar doctor por ID.

### **Citas**
- **GET** `/citas`: Lista todas las citas.
- **GET** `/citas/{cita_id}`: Detalles de una cita por ID.
- **POST** `/citas`: Crear una nueva cita.
- **PUT** `/citas/{cita_id}`: Actualizar una cita.
- **DELETE** `/citas/{cita_id}`: Eliminar cita.

### **Login**
- **POST** `/login`: Autenticar usuario.

## **Instrucciones de Instalación**

### **Requisitos**
- Python 3.7+
- Dependencias: FastAPI, SQLAlchemy, Pydantic, Uvicorn

### **Pasos para Ejecutar**

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ThairConstante/API-Citas.git
   cd API-Citas

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

3. Ejecutar el servidor:
   ```bash
   uvicorn main:app --reload

4. Acceder a la documentación interactiva:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

5. Accede al Frontend:
Abre el archivo index.html en la carpeta frontend/ de este repositorio en tu navegador. Asegúrate de que la API esté ejecutándose en http://127.0.0.1:8000.
   
### **Ejemplo de Uso**

#### Crear un Usuario
#### **Petición**
- **Método**: POST
- **Endpoint**: `/usuarios`
- **Cuerpo**:
  ```json
  {
    "username": "juan",
    "password": "mi_contraseña_segura",
    "email": "juan@ejemplo.com"
  }
  ```

#### **Respuesta Exitosa**
```json
{
  "username": "juan",
  "email": "juan@ejemplo.com"
}
```
## Colaboradores
- Thair Constante Pineda  
- Kenny Vivero Pomares 