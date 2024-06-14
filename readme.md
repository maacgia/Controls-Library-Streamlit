### Biblioteca de Controles en Streamlit

Bienvenido a la Biblioteca de Controles en Streamlit. Este repositorio está diseñado como una guía completa para ayudarte a construir aplicaciones interactivas con Streamlit, demostrando una amplia variedad de controles y funcionalidades que puedes utilizar en tus propios proyectos.

#### Contenido

- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación y Configuración](#instalación-y-configuración)
- [Descripción de Páginas](#descripción-de-páginas)
- [Uso de Docker](#uso-de-docker)
- [Créditos](#créditos)

### Requisitos

- Docker y Docker Compose instalados en tu máquina.
- Conexión a Internet para descargar las dependencias.

### Estructura del Proyecto

```
.
├── docker-compose.yml
├── Dockerfile
├── app
│   ├── app.py
│   ├── page1.py
│   ├── page2.py
│   ├── page3.py
│   ├── page4.py
│   ├── page5.py
│   └── requirements.txt
└── README.md
```

### Instalación y Configuración

#### Paso 1: Clonar el repositorio

Clona este repositorio en tu máquina local usando:

```sh
git clone https://github.com/maacgia/Controls-Library-Streamlit
cd Controls-Library-Streamlit
```

#### Paso 2: Configurar Docker

Asegúrate de que Docker y Docker Compose estén instalados en tu sistema. Luego, puedes construir y levantar los contenedores usando:

```sh
docker compose up --build
```

Este comando construirá la imagen de Docker y levantará el contenedor definido en `docker-compose.yml`.

### Descripción de Páginas

#### Página 1: Controles Básicos

Esta página demuestra cómo utilizar controles básicos de Streamlit, incluyendo botones, checkboxes, radio buttons, select boxes, sliders, y más.

#### Página 2: Controles Adicionales

Aquí encontrarás ejemplos de controles adicionales como la carga de archivos, la selección de colores, la entrada de texto en varias líneas, y gráficos de mapas de calor.

#### Página 3: Controles Adicionales Avanzados

Esta página muestra ejemplos de controles más avanzados, como select sliders, controles de audio y video, entrada de cámara, métricas, y formularios.

#### Página 4: Menús de Navegación

En esta página se demuestra cómo crear menús de navegación verticales, horizontales y personalizados usando `streamlit-option-menu`.

#### Página 5: Controles y Funcionalidades Adicionales

La última página incluye ejemplos de visualización de datos geoespaciales, gráficos interactivos con Plotly y Altair, integración con Folium para mapas avanzados, carga y visualización de imágenes, almacenamiento en caché, y un ejemplo básico de autenticación.

### Uso de Docker

#### Archivo `docker-compose.yml`

```yaml

services:
  bibliotec_streamlit:
    build: .
    container_name: bibliotec_streamlit
    image: bibliotec_streamlit:dev

    volumes:
      - ./app:/app
    ports:
      - 8501:8501
    stdin_open: true  # Mantiene el contenedor abierto para entrada estándar
    tty: true  # Mantiene el contenedor en ejecución

```

#### Archivo `Dockerfile`

```dockerfile
FROM python:3.9-slim

COPY ./app /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]

```

#### Comandos para Ejecutar

Para construir y ejecutar el contenedor Docker, usa:

```sh
docker-compose up --build
```

# Acceso a la Aplicación
Una vez que el contenedor Docker esté en ejecución, puedes acceder a la aplicación Streamlit en tu navegador web usando la siguiente URL:


```
http://localhost:8501
```

Asegúrate de sustituir localhost con la dirección IP o nombre de host correspondiente si estás ejecutando Docker en una máquina remota.

### Créditos

Este proyecto fue desarrollado como una herramienta educativa para ayudar a los desarrolladores a explorar y utilizar las capacidades de Streamlit. Si tienes alguna pregunta o sugerencia, no dudes en crear un issue o contribuir al proyecto.

---

Con estos pasos, deberías estar listo para empezar a utilizar y experimentar con los diversos controles y funcionalidades que Streamlit ofrece. ¡Feliz codificación!