# flights-elt-medallion-pipeline

ELT pipeline implementing **Medallion Architecture** (**Bronze, Silver, Gold**) to process airline transaction data and identify the most frequently used airlines based on transaction counts.

The pipeline is orchestrated using **Apache Airflow**, declarative SQL transformations, Python components, and scalable processing concepts in the Silver layer.

---

# Project Overview

This project implements an ELT pipeline using the Medallion Architecture (**Bronze, Silver, Gold**) to process and analyze airline ticketing data.

The goal of the project is to transform raw airline transaction data into a clean and aggregated dataset that enables analysis of airline popularity based on transaction volume.

The pipeline executes transformations sequentially across Bronze, Silver, and Gold layers.

Workflow orchestration is managed using **Apache Airflow DAGs**.

---

# Initial Problem Statement

Airline ticketing data is often stored in raw and inconsistent formats, making it difficult to analyze trends such as the most frequently used airlines.

The objective of this project is to clean and transform the data in order to identify which airlines generate the highest number of transactions and support further analytical use cases.

---

# Dataset

The dataset used in this project is available on Kaggle:

https://www.kaggle.com/datasets/jayitabhattacharyya/hackerearth-arcenter-the-travelverse/data

It contains airline ticketing data including:

* transaction_key
* ticketing_airline
* agency
* issue_date
* origin
* destination
* cabin

---

# Architecture (Medallion)

The pipeline follows the Medallion Architecture:

**Bronze (TRAVEL_RAW)** – raw ingested data

**Silver (AIRLINE, ROUTE, FACT_TRAVEL)** – cleaned and structured data model

**Gold (TRAVEL_GOLD)** – aggregated data for analytics

Data flows sequentially:

```text id="a81f5m"
Bronze → Silver → Gold
```

---

## Architecture Diagram

![Architecture](high-level-architecture.png)

## Data Model

![Data Model](db-architecture.png)

---

# Workflow Orchestration (Apache Airflow)

The pipeline is orchestrated using **Apache Airflow**.

Airflow manages task dependencies, scheduling, monitoring, and pipeline execution through a DAG.

Execution order:

1. Bronze layer ingestion
2. Silver layer transformations
3. Gold layer aggregation

## Airflow DAG

![Airflow DAG](airflow/airflow-dag.png)

## Successful Pipeline Run

![Airflow Success](airflow/airflow-success.png)

---

# Processing Engine

The Silver layer uses scalable processing concepts for transformations and business logic execution.

This layer represents the transformation zone between raw operational data and analytics-ready outputs.

---

# Pipeline Execution Flow

The pipeline executes in the following order:

## Bronze

* create_schema.sql
* create_stage.sql
* create_stage_table.sql
* load_stage.sql
* create_tables.sql
* load_bronze.sql

## Silver

* data transformation logic
* data cleaning
* standardization
* dimensional modeling

## Gold

* create_tables.sql
* aggregation query (TRAVEL_GOLD)

The pipeline is executed sequentially using Apache Airflow orchestration.

---

# Data Pipeline

1. Load raw data into TRAVEL_RAW
2. Clean and transform data in Silver layer
3. Create dimension tables AIRLINE and ROUTE
4. Create fact table FACT_TRAVEL
5. Aggregate data to create TRAVEL_GOLD

---

# Data Cleaning (Silver Layer)

The following transformations were applied:

* Removed NULL values from transaction_key
* Removed duplicates using DISTINCT
* Trimmed text fields
* Converted issue_date to DATE format
* Standardized airline names
* Standardized route data

---

# Aggregation (Gold Layer)

The Gold layer joins fact and dimension tables and aggregates the data to calculate the number of transactions per airline and route.

This layer produces analytics-ready data.

---

# Idempotency Strategy

The pipeline is designed to be idempotent:

* Bronze layer uses repeatable ingestion logic
* Silver layer uses deterministic transformations
* Gold layer uses repeatable aggregation logic
* Tables created using CREATE IF NOT EXISTS
* Pipeline can be safely re-run multiple times

---

# Technologies Used

* Python
* SQL
* Apache Airflow
* Docker
* Apache Spark concepts (Silver layer)
* Snowflake-ready ELT design
* Medallion Architecture
* GitHub

---

# Repository Structure

```text id="pmmx2j"
bronze/          - raw ingestion layer
silver/          - cleaned and structured tables
gold/            - aggregated analytics layer
orchestration/   - python pipeline scripts

airflow/
 ├── dags/
 ├── docker-compose.yml
 ├── airflow-dag.png
 └── airflow-success.png

db-architecture.png
high-level-architecture.png
README.md
```

---

# How to Run

Clone the repository:

```bash id="skkvlk"
git clone <repo>
cd flights-elt-medallion-pipeline
```

Start Airflow:

```bash id="m3qf0w"
cd airflow
docker compose up
```

Open UI:

```text id="0p4j38"
http://localhost:8080
```

Trigger DAG:

```text id="xk4y3q"
flights_pipeline
```

---

# Why This Project Matters

This repository demonstrates practical Data Engineering skills:

* workflow orchestration
* DAG dependency management
* layered architecture
* ELT pipeline design
* production-style project structure
* maintainable repository design

---

# Future Improvements

* CI/CD deployment
* automated tests
* dbt integration
* cloud deployment (AWS / Azure / GCP)
* monitoring & alerting
* real distributed Spark runtime

---

# Author

**Julia Kramek**
