# Utiliza la imagen base de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos a la imagen
COPY requirements.txt .

# Instala las dependencias del archivo de requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación a la imagen
COPY . .

# Exponer el puerto 3030
EXPOSE 3030

# Comando para ejecutar la aplicación con gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:3030", "app:app"]
