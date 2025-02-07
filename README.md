# HAVIVI

## Configuración Inicial/Instalación
- Instalar Docker
- Clonar repositorio
- Abrir la carpeta del proyecto con Visual Studio Code
- Generar imagen de Docker desde la terminal de VS Code
    - ``docker build -t havivi-docker:latest .``

## Correr el servidor
- Correr el contenedor
    - ``docker run -p 8000:8000 --env PIPELINE=local havivi-docker``
- Abrir en el navegador
    - ``http://127.0.0.1:8000/``