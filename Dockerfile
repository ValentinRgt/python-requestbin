FROM python:alpine

WORKDIR /app

COPY app.py /app/app.py

RUN mkdir /app/logs

RUN pip install Flask

EXPOSE 5000

CMD ["python", "app.py"]