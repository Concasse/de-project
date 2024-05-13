FROM python:3.9.1

RUN apt-get update && apt-get install -y
RUN pip install pandas sqlalchemy pyarrow psycopg2 argparse

WORKDIR /app
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]