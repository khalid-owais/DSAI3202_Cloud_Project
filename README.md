# DSAI3202_Cloud_Project
# NYC Yellow Taxi Data Pipeline (March 2016)

## Introduction
This project implements a reproducible ETL pipeline for NYC Yellow Taxi data using Azure Databricks and the Medallion Architecture (Bronze → Silver → Gold). The goal is to prepare clean, curated, and feature‑rich datasets for analytics and machine learning.

## Pipeline Overview
1. **Bronze**: Raw CSV ingested from Azure Blob Storage.
2. **Silver**: Cleaned and validated Parquet data.
3. **Gold**: Curated feature dataset ready for ML.

## Steps
- **Notebook 01**: Load & Clean trips.
- **Notebook 02**: Enrich with time and efficiency features.
- **Notebook 03**: Curate Gold dataset.
- **Notebook 04**: Sample ~300k trips for ML.
- **Notebook 05**: Feature engineering (weekend flag, average speed).

## Schema
- `tpep_pickup_datetime` (datetime)
- `tpep_dropoff_datetime` (datetime)
- `trip_distance` (float)
- `trip_duration_minutes` (float)
- `fare_amount` (float)
- `pickup_hour` (int)
- `pickup_day_of_week` (int)
- `fare_per_mile` (float)
- `is_weekend` (int)
- `avg_speed_mph` (float)

## Assumptions
- Trips with negative fares or distances are invalid.
- Trips longer than 3 hours or >50 miles flagged as outliers.
- Raw data always preserved in Bronze.

## Results
- Distribution plots of distance and fare.
- Correlation heatmap between distance, fare, duration.
- Sampled dataset (`features_v1_sampled`) and engineered dataset (`features_v2`).

## How to Reproduce
1. Run notebooks in sequence on Databricks.
2. Verify outputs in blob storage containers:
   - `processed/clean_trips/`
   - `processed/enriched_trips/`
   - `curated/features_v1/`
   - `curated/features_v1_sampled/`
   - `curated/features_v2/`
