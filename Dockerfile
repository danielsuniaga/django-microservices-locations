# Usa una imagen base ligera de Python
FROM python:3.8

# Agrega el script para esperar a que los servicios estén disponibles (ej. base de datos)
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /code

# Instalamos Poetry
RUN pip install --upgrade pip && pip install poetry

# Configuramos Poetry para crear el entorno virtual dentro del proyecto
RUN poetry config virtualenvs.in-project true

# Copiamos el archivo pyproject.toml
COPY pyproject.toml poetry.lock* /code/

# Instalamos las dependencias del proyecto utilizando Poetry
RUN poetry install --no-dev --verbose

# Copiamos el resto del código fuente al contenedor
COPY . /code/

# Establecemos el directorio de trabajo al entorno virtual de Poetry
ENV VIRTUAL_ENV=/code/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Esperamos que la base de datos esté lista antes de ejecutar el servidor
CMD ["/usr/local/bin/wait-for-it.sh", "database:${DB_PORT}", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
