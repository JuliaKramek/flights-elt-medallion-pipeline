# flights-elt-medallion-pipeline

Production-style ELT pipeline based on the **Medallion Architecture** (**Bronze → Silver → Gold**) for processing airline transaction data and identifying the most frequently used airlines.

The project demonstrates modern data engineering practices including:

* Layered data architecture
* Workflow orchestration with **Apache Airflow**
* SQL-based transformations
* Python pipeline components
* Scalable processing concepts (Spark-ready Silver layer)
* Re-runnable / idempotent pipeline design

---

# Project Goal

Airline transaction data is often stored in raw and inconsistent formats, making analytics difficult.

The goal of this project is to transform raw records into clean, structured, and aggregated datasets that answer business questions such as:

* Which airlines are used most frequently?
* Which routes generate the most transactions?
* How can raw operational data be converted into analytics-ready tables?

---

# Medallion Architecture

The pipeline follows the Medallion model:

## Bronze Layer

Raw ingested source data.

Examples:

* original transactions
* unchanged raw records
* landing zone tables

## Silver Layer

Cleaned and standardized business model.

Examples:

* removed duplicates
* handled null values
* standardized airline names
* transformed routes
* structured dimension/fact model

## Gold Layer

Aggregated analytics-ready output.

Examples:

* top airlines by transaction volume
* route statistics
* reporting tables

---

# Workflow Orchestration (Apache Airflow)

The pipeline is orchestrated with **Apache Airflow** as a DAG consisting of three sequential tasks:

```text
bronze → silver → gold
```

## Airflow DAG

![Airflow DAG](images/airflow-dag.png)

## Successful Pipeline Run

![Airflow Success](images/airflow-success.png)

---

# Technical Architecture

![Architecture](images/high-level-architecture.png)

---

# Data Model

![Data Model](images/db-architecture.png)

---

# Repository Structure

```text
flights-elt-medallion-pipeline/
│── bronze/                 # raw ingestion SQL
│── silver/                 # transformation layer SQL
│── gold/                   # aggregation layer SQL
│── orchestration/          # python pipeline scripts
│── airflow/
│   ├── dags/              # airflow DAG definitions
│   └── docker-compose.yml # local airflow setup
│── images/                # screenshots / diagrams
│── README.md
```

---

# Technologies Used

* Python
* SQL
* Apache Airflow
* Docker
* Apache Spark (Silver layer concept)
* Snowflake-ready ELT design
* GitHub

---

# Pipeline Flow

```text
Raw Data
   ↓
Bronze
   ↓
Silver
   ↓
Gold
   ↓
Analytics / Reporting
```

---

# Data Quality Rules (Silver Layer)

Applied transformations include:

* NULL filtering
* duplicate removal
* field standardization
* schema cleanup
* route normalization
* business-ready formatting

---

# Idempotency

The pipeline is designed to be safely re-run.

Features:

* deterministic transformations
* repeatable SQL logic
* CREATE IF NOT EXISTS patterns
* stable task ordering in Airflow

---

# How to Run Locally

## 1. Clone repository

```bash
git clone <your-repository-url>
cd flights-elt-medallion-pipeline
```

## 2. Start Airflow

```bash
cd airflow
docker compose up
```

## 3. Open UI

```text
http://localhost:8080
```

## 4. Trigger DAG

Run:

```text
flights_pipeline
```

---

# Why This Project Matters

This repository demonstrates practical skills expected in Data Engineering roles:

* pipeline orchestration
* DAG dependency management
* layered architecture
* ETL / ELT thinking
* production-style project structure
* maintainable repository design

---

# Future Improvements

* real Spark cluster integration
* automated tests
* CI/CD deployment
* dbt transformations
* data quality monitoring
* cloud deployment (AWS / Azure / GCP)

---

# Author

**Julia Kramek**
