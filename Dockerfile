FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

#RUN apt-get update \
#    && apt-get install gcc -y \
#    && apt-get clean

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/

#RUN adduser -D myuser
#USER myuser

#CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", $PORT]
CMD uvicorn app.server:app --host 0.0.0.0 --port $PORT

