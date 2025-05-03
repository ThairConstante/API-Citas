-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS `db_citas_medicas` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_citas_medicas`;

-- Tabla: usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insertar datos de ejemplo: usuarios
INSERT INTO `usuarios` (`nombre`, `username`, `password`) VALUES
('Thair constante', 'thair@gmail.com', '1234'),
('Kenny vivero', 'kenny@gmail.com', '1234');

-- Tabla: pacientes
CREATE TABLE IF NOT EXISTS `pacientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `identificacion` varchar(25) NOT NULL,
  `sexo` varchar(25) NOT NULL,
  `edad` varchar(25) NOT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insertar datos de ejemplo: pacientes
INSERT INTO `pacientes` (`nombre`, `identificacion`, `sexo`, `edad`, `correo`, `telefono`) VALUES
('María Pérez', '123456789', 'Femenino', '35', 'maria.perez@gmail.com', '3011234567'),
('Carlos Gómez', '987654321', 'Masculino', '42', 'carlos.gomez@yahoo.com', '3029876543');

-- Tabla: doctores
CREATE TABLE IF NOT EXISTS `doctores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `identificacion` varchar(25) DEFAULT NULL,
  `especialidad` varchar(100) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insertar datos de ejemplo: doctores
INSERT INTO `doctores` (`nombre`, `identificacion`, `especialidad`, `correo`) VALUES
('Dra. Andrea Torres', '11223344', 'Medicina General', 'atorres@clinicamed.com'),
('Dr. Juan Martínez', '22334455', 'Cardiología', 'jmartinez@clinicamed.com');

-- Tabla: citas
CREATE TABLE IF NOT EXISTS `citas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paciente_id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `estado` int(11) DEFAULT NULL COMMENT '0: pendiente, 1: realizada, 2: cancelada',
  `observaciones` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `paciente_id` (`paciente_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `citas_ibfk_1` FOREIGN KEY (`paciente_id`) REFERENCES `pacientes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `citas_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctores` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Insertar datos de ejemplo: citas
INSERT INTO `citas` (`paciente_id`, `doctor_id`, `fecha`, `hora`, `estado`, `observaciones`) VALUES
(1, 1, '2025-05-05', '10:00:00', 0, 'Paciente con síntomas gripales'),
(2, 2, '2025-05-06', '11:30:00', 1, 'Control de presión arterial');

