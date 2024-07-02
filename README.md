# Turismo EV3 DUOC

Este proyecto es una aplicación web para una empresa de turismo extremo en Chile. Está desarrollada utilizando Flask, Bootstrap 4 y MariaDB. La aplicación permite a los usuarios registrarse, enviar sugerencias o quejas, y ver un catálogo de deportes de aventura. Los administradores pueden ver y gestionar los usuarios y las sugerencias.

## Requisitos

- Python 3
- Flask
- Bootstrap 4
- MariaDB
- Virtualenv

## Estructura del Proyecto

```
flask_app/
│
├── app.py
├── static/
│   └── img/
│       ├── MENU2.jpg
│       ├── Nieve.jpg
│       ├── LOGOTURISMO.png
│       ├── rafting.jpg
│       ├── trekking.jpg
│       ├── paracaidas.jpg
│       └── corralco.jpg
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── suggestions.html
│   ├── admin.html
│   └── catalog.html
└── venv/
```

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Panchetos69/Turismo-EV3-duoc.git
cd Turismo-EV3-duoc
```

2. Crea y activa un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install Flask flask-mysqldb
```

4. Configura MariaDB:

```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

5. Inicia sesión en MariaDB y crea la base de datos y las tablas:

```sql
CREATE DATABASE turismo_app;

USE turismo_app;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(12) NOT NULL,
    nombre_completo VARCHAR(100) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(10) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL
);

CREATE TABLE suggestions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    correo_electronico VARCHAR(100) NOT NULL,
    mensaje TEXT NOT NULL
);

CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    comentario TEXT NOT NULL
);
```

## Uso

1. Ejecuta la aplicación Flask:

```bash
python app.py
```

2. Abre tu navegador y navega a `http://localhost:5000` para ver la aplicación.

## Funcionalidades

### Usuarios

- Registro de usuarios con validación de datos.
- Visualización y gestión de usuarios en el panel de administración.

### Sugerencias

- Envío de sugerencias o quejas por parte de los usuarios.
- Visualización de sugerencias en el panel de administración.

### Catálogo

- Visualización de un catálogo de deportes de turismo aventura con imágenes y descripciones.

### Administración

- Panel de administración para gestionar usuarios y sugerencias.
- Envío de comentarios desde el panel de administración.

## Contribuir

Si deseas contribuir a este proyecto, por favor, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios necesarios y haz un commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.


## Contacto

Si tienes alguna pregunta o sugerencia, por favor, contacta al autor del proyecto 
```

Este `README.md` proporciona una descripción general del proyecto, instrucciones de instalación y uso, y detalles sobre cómo contribuir. Asegúrate de ajustar las secciones de contacto y contribuciones según sea necesario para tu proyecto específico.
