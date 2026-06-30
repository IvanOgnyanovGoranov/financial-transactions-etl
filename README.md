# Financial Transactions ETL Pipeline

A payments data pipeline built to learn data engineering fundamentals.
First hands-on project with Docker and Airflow.

## What it does
Takes synthetic financial transaction data (PaySim, 500k rows), loads it
into PostgreSQL, then transforms it into a cleaned table with two derived
fraud-detection columns - transactions the system missed and balance
anomalies.

## Stack
Python · PostgreSQL 15 · Airflow · Docker · pandas · SQLAlchemy

## How to run
1. Clone the repo and create `.env` from `.env.example`
2. `docker compose up -d`
3. Create the database and tables using scripts in `sql/`
4. `python -m src.ingest`
5. `python -m src.transform`

## Dataset
PaySim synthetic mobile money transactions — https://www.kaggle.com/datasets/ealaxi/paysim1

## Future improvements
- PostgreSQL COPY for faster ingestion
- Power BI dashboard
- Unit tests
