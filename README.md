# flights-elt-medallion-pipeline

ELT pipeline implementing Medallion Architecture (Bronze, Silver, Gold) to process airline transaction data and identify the most frequently used airlines based on transaction counts.
The pipeline is orchestrated using a Python entrypoint and declarative SQL transformations.

---

# Project Overview

This project implements an ELT pipeline using the Medallion Architecture (Bronze, Silver, Gold) to process and analyze airline ticketing data.

The goal of the project is to transform raw airline transaction data into a clean and aggregated dataset that enables analysis of airline popularity based on transaction volume.

The pipeline is orchestrated using Python and executes SQL transformations sequentially across Bronze, Silver, and Gold layers.

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

Data flows sequentially from Bronze → Silver → Gold.

---

## Architecture Diagram

![Architecture](high-level-architecture.png)

## Data Model

![Data Model](db-architecture.png)

# Orchestration

The pipeline is orchestrated using a Python entrypoint:

```
python orchestration/run_pipeline.py
```

Execution order:

1. Bronze layer ingestion
2. Silver layer transformations
3. Gold layer aggregation

Each layer executes declarative SQL transformations.

---

# Pipeline Execution Flow

The pipeline executes SQL scripts in the following order:

## Bronze

* create_schema.sql
* create_stage.sql
* create_stage_table.sql
* load_stage.sql
* create_tables.sql
* load_bronze.sql

## Silver

* create tables
* transform data
* build dimension AIRLINE
* build dimension ROUTE
* build FACT_TRAVEL

## Gold

* create_tables.sql
* aggregation query (TRAVEL_GOLD)

The pipeline is executed sequentially using Python orchestrator.

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
* Trimmed text fields (ticketing_airline, agency)
* Converted issue_date to DATE format
* Standardized airline names
* Standardized route data

---

# Aggregation (Gold Layer)

The Gold layer joins the fact and dimension tables and aggregates the data to calculate the number of transactions per airline and route.

This layer produces analytics-ready data.

---

# Idempotency Strategy

The pipeline is designed to be idempotent:

* Bronze layer uses append-only ingestion with batch_id
* Silver layer uses deterministic transformations
* Gold layer uses MERGE to avoid duplicates
* Tables created using CREATE IF NOT EXISTS
* Pipeline can be safely re-run multiple times

---

# Data Quality Risks

1. Duplicate transaction keys may lead to incorrect aggregations
2. Missing values in transaction_key
3. Invalid or inconsistent date formats in issue_date
4. Inconsistent airline naming conventions
5. Missing route information

---

# Technologies Used

* Python (pipeline orchestration)
* SQL (data transformations)
* Snowflake
* Medallion Architecture
* ELT pipeline design
* GitHub

---

# Repository Structure

```
bronze/          - raw ingestion layer  
silver/          - cleaned and structured tables  
gold/            - aggregated analytics layer  
orchestration/   - pipeline orchestrator (Python)  

DB Architecture.png  
High-Level Data Architecture.png  
README.md  
```

---

# How to Run

Clone the repository:

```
git clone <repo>
```

Go to project directory:

```
cd flights-elt-medallion-pipeline
```

Run pipeline:

```
python orchestration/run_pipeline.py
```

---

# Pipeline Flow

```
Raw Data
   ↓
Bronze
   ↓
Silver
   ↓
Gold
   ↓
Analytics
```

---

# Author

Julia Kramek
