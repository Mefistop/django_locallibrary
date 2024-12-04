FROM python:3.11
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY locallibrary .

RUN python manage.py collectstatic --noinput
RUN python manage.py loaddata data.json
CMD ["gunicorn", "locallibrary.wsgi:application", "--bind", "0.0.0.0:8000"]
