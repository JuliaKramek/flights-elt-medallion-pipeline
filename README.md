# flights-elt-medallion-pipeline
ELT pipeline in Snowflake using Medallion Architecture (Bronze, Silver, Gold) to analyze airline transaction data and identify the most frequently used airlines based on transaction counts.


## Project Overview

This project implements an ELT pipeline in Snowflake using the Medallion Architecture (Bronze, Silver, Gold) to process and analyze airline ticketing data.

The goal of the project is to transform raw airline transaction data into a clean and aggregated dataset that enables analysis of airline popularity based on transaction volume.


## Initial Problem Statement

Airline ticketing data is often stored in raw and inconsistent formats, making it difficult to analyze trends such as the most frequently used airlines.

The objective of this project is to clean and transform the data in order to identify which airlines generate the highest number of transactions and support further analytical use cases.

## Dataset

The dataset used in this project is available on Kaggle:
https://www.kaggle.com/datasets/jayitabhattacharyya/hackerearth-arcenter-the-travelverse/data

It contains airline ticketing data including:

* transaction_key
* ticketing_airline
* agency
* issue_date

## Architecture (Medallion)

The pipeline follows the Medallion Architecture:

* **Bronze (TRAVEL_RAW)** – raw ingested data  
* **Silver (AIRLINE, ROUTE, FACT_TRAVEL)** – cleaned and structured data model  
* **Gold (TRAVEL_GOLD)** – aggregated data for analytics
  
## Data Pipeline

1. Load raw data into `TRAVEL_RAW`
2. Create dimension tables `AIRLINE`, `ROUTE`
3. Create fact table `FACT_TRAVEL`
4. Aggregate data to create `TRAVEL_GOLD`


## Data Cleaning (Silver Layer)

The following transformations were applied:

* Removed NULL values from `transaction_key`
* Removed duplicates using `DISTINCT`
* Trimmed text fields (`ticketing_airline`, `agency`)
* Converted `issue_date` to DATE format using `TRY_TO_DATE`


## Aggregation (Gold Layer)

The Gold layer joins the fact and dimension tables and aggregates the data to calculate the number of transactions per airline and route.


## Data Quality Risks

1. Duplicate transaction keys may lead to incorrect aggregations
2. Missing values (NULLs) in key fields such as `transaction_key` or `ticketing_airline`
3. Invalid or inconsistent date formats in the `issue_date` column


## Technologies Used

* Snowflake
* SQL
* GitHub


## Repository Structure

* `bronze/` – raw ingestion layer  
* `silver/` – structured tables (AIRLINE, ROUTE, FACT_TRAVEL)  
* `gold/` – aggregated analytics layer  
* `DB Architecture.png` – architecture diagram  
* `README.md` – project documentation  

## Author

Julia Kramek
