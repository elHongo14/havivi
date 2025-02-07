FROM python:3.13.1
ENV PYTHONBUFFERED=1
ENV PORT 8000
WORKDIR /app
COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD gunicorn havivi_proj.wsgi:application --bind 0.0.0.0:"${PORT}"
EXPOSE ${PORT}