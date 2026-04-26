# flights-elt-medallion-pipeline

ELT pipeline implementing **Medallion Architecture** (**Bronze, Silver, Gold**) to process airline transaction data and identify the most frequently used airlines based on transaction counts.

The project demonstrates workflow orchestration using **Apache Airflow**, layered data modeling, and SQL-based transformations, extended with **real-time streaming using Apache Kafka**.

---

# Project Overview

This project implements an **ELT pipeline** using the Medallion Architecture (**Bronze, Silver, Gold**) to process and analyze airline ticketing data.

The objective is to transform raw airline transaction data into structured and analytics-ready datasets that support business insights such as:

* airline popularity
* transaction volumes
* popular routes
* customer booking behavior

The pipeline executes sequentially across Bronze, Silver, and Gold layers and is orchestrated using **Apache Airflow**, while streaming ingestion is handled independently via **Kafka**.

---

# Initial Problem Statement

Airline ticketing data is often stored in raw and inconsistent formats, making it difficult to analyze operational trends.

The purpose of this project is to clean, standardize, and aggregate the data into a usable analytical model.

---

# Dataset

The dataset used in this project is publicly available on Kaggle:

https://www.kaggle.com/datasets/jayitabhattacharyya/hackerearth-arcenter-the-travelverse/data

It contains airline ticketing data including:

* transaction_key
* ticketing_airline
* marketing_airline
* agency
* issue_date
* departure_date
* origin
* destination
* country
* cabin

---

# Technologies

* Apache Airflow – workflow orchestration and scheduling
* PostgreSQL – data storage and SQL transformations
* Kafka – real-time streaming ingestion
* Python – DAG creation and Kafka producer/consumer
* Docker Compose – local containerized environment
* SQL – schema creation, loading, transformation, aggregation
* GitHub – version control and project delivery

---

# Architecture (Medallion)

The pipeline follows the **Medallion Architecture**.

## Bronze Layer

Raw ingested source data stored in:

`bronze.travel_raw`

Purpose:

* preserve source records
* enable traceability
* act as ingestion layer

All columns are stored as **TEXT** to ensure fault-tolerant ingestion from both batch and streaming sources.

## Silver Layer

Cleaned and structured relational model:

* AIRLINE
* ROUTE
* FACT_TRAVEL

Purpose:

* remove duplicates
* clean null values
* standardize columns
* prepare analytical model

## Gold Layer

Aggregated reporting table:

`gold.travel_gold`

Purpose:

* business-ready analytics
* KPI reporting
* top airlines ranking

---

# Data Ingestion Strategy

The pipeline supports two ingestion modes:

* **Batch ingestion (Airflow)** – used for historical data loading
* **Streaming ingestion (Kafka)** – used for incremental real-time data

Both ingestion methods write to the same Bronze layer, ensuring a unified and consistent data entry point.

---

# Data Flow

Batch (Airflow) + Streaming (Kafka) → Bronze → Silver → Gold

---

# Streaming (Kafka)

The project includes a streaming module responsible for real-time ingestion.

Structure:

```id="ijmztr"
streaming/
├── producer.py
└── consumer.py
```

* **Producer** reads data and sends it to a Kafka topic
* **Consumer** listens to the topic and inserts data into `bronze.travel_raw`
* Streaming operates independently from Airflow

This enables:

* near real-time ingestion
* scalable and decoupled architecture
* continuous data updates

---

# Architecture Diagram

![Architecture](high-level-architecture.png)

---

# Data Model

![Data Model](db-architecture.png)

---

# Workflow Orchestration (Apache Airflow)

The pipeline is orchestrated using **Apache Airflow**.

Airflow is responsible for:

* task sequencing
* dependency management
* scheduled / manual execution
* monitoring runs
* retry handling

Pipeline Execution Order:

1. Bronze ingestion
2. Silver transformations
3. Gold aggregation

---

# Airflow DAG

![Airflow DAG](airflow/airflow-dag.png)

---

# Successful Run

![Airflow Success](airflow/airflow-success.png)

---

# Pipeline Execution Flow

## Bronze

Responsible for raw ingestion and staging.

Executed steps:

* create_schema.sql
* create_stage.sql
* create_stage_table.sql
* load_stage.sql
* create_tables.sql
* load_bronze.sql

## Silver

Responsible for cleansing, transformation, and structured modeling.

Includes:

* removing duplicates
* trimming text values
* handling nulls
* standardizing columns
* date conversion
* loading fact and dimension tables

## Gold

Responsible for business-ready aggregation.

Includes:

* create_schema.sql
* create_tables.sql
* load_gold.sql

---

# Data Pipeline Logic

1. Raw source data loaded into Bronze layer
2. Data cleaned and standardized in Silver layer
3. Dimension tables created
4. Fact table populated
5. Gold layer aggregates transactions by airline

---

# Data Cleaning (Silver Layer)

Applied transformations:

* removed NULL transaction keys
* removed duplicates
* trimmed text columns
* standardized airline names
* standardized route values
* converted date fields to DATE format
* prepared dimensional model

---

# Aggregation (Gold Layer)

The Gold layer calculates:

* total transactions per airline
* route usage metrics
* analytical summary outputs

This creates an analytics-ready dataset for BI and reporting purposes.

##  Data Quality Metrics

- Completeness of transaction_key > 98%
- Uniqueness of transaction_key = 100%
- Data freshness < 2 days

---

# How to Run

## Clone Repository

git clone <repo-url>
cd flights-elt-medallion-pipeline

## Start Environment

docker compose up

## Open Airflow UI

http://localhost:8080

## Trigger DAG

flights_pipeline

---

# Author

Julia Kramek
