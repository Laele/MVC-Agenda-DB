#Definition of the schema of the DB

#Create the DB
CREATE DATABASE IF NOT EXISTS agenda_db;

#Select the database to work with
USE agenda_db;

#Create the kernel tables
 CREATE TABLE IF NOT EXISTS Contacto (
  id_contacto int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  nombre varchar(35) NOT NULL,
  apellido_paterno varchar(35) NOT NULL,
  apellido_materno varchar(35),
  correo varchar(50),
  telefono varchar(10)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS  Cita (
  id_cita int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  fecha datetime NOT NULL,
  asunto varchar(255),
  ubicacion varchar(255),
  id_contacto int,
  CONSTRAINT fkid_contacto_Cita FOREIGN KEY(id_contacto)
	REFERENCES Contacto(id_contacto)
    ON DELETE SET NULL
    ON UPDATE CASCADE
)ENGINE = INNODB;

#ALTER TABLE Cita ADD FOREIGN KEY (id_contacto) REFERENCES Contacto (id_contacto);