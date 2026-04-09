# NYC Taxi Fare Prediction: End-to-End Azure ML Pipeline

## 1. Project Overview
This project demonstrates a professional machine learning lifecycle using the Microsoft Azure ecosystem. We transformed raw NYC Taxi data into a high-accuracy predictive service, achieving a 76.4% reduction in error compared to the baseline.

## 2. Data Governance & Lineage
To ensure traceability and reliability (Requirement II.3), the data followed a strict lifecycle:
* **Source:** NYC Taxi & Limousine Commission (Kaggle Dataset).
* **Raw Layer:** Initial Parquet files stored in Azure Data Lake Storage (ADLS) Gen2.
* **Silver Layer:** Cleaned using Databricks Spark. We removed trips with 0-mile distances and negative fare amounts to ensure data integrity.
* **Gold Layer:** Final feature-engineered dataset registered as `taxi_gold_ds` in the Azure ML Data catalog.

## 3. Feature Engineering Justification
The baseline model struggled because it ignored temporal and traffic factors. We engineered the following features to capture the complexity of NYC traffic:
* **trip_duration_mins:** Provides a proxy for traffic congestion and wait times.
* **pickup_hour:** Accounts for rush-hour surcharges and peak demand periods.
* **day_of_week:** Captures the variation between weekday business travel and weekend leisure travel.

## 4. Modeling Results
We validated our features by comparing a simple Linear Regression against a Random Forest Regressor.

| Metric | Baseline Model | Full-Feature Model | Improvement |
| :--- | :--- | :--- | :--- |
| **RMSE** | $10.55 | **$2.49** | **76.4%** |
| **Features** | Distance, Passengers | Distance, Passengers, Hour, Day, Duration | |

**Conclusion:** The transition to a tree-based ensemble model with time-aware features allows for highly accurate fare estimates, crucial for real-time ride-sharing applications.

## 5. Deployment & Validation
* **Model Registry:** The trained model is registered as `taxi_fare_predictor` (Version 1) and is linked to the `taxi_gold_ds` for full lineage.
* **Inference Pipeline:** A production-ready `score.py` script and `env.yml` environment were authored to handle real-time API requests.
* **Deployment Status:** While final ACI (Azure Container Instance) provisioning was restricted by subscription-level permissions (403 AuthorizationFailed), the deployment scripts were fully validated.
* **Local Validation:** The inference logic was tested in the Azure ML environment, successfully returning a predicted fare of **$17.30** for a standard 5-mile trip.

## 6. Repository Structure
* `Phase1_ETL.ipynb`: Spark-based data cleaning and enrichment.
* `Phase2_Model_Training.ipynb`: Model training, registration, and deployment validation.
* `score.py`: The entry script for the scoring web service.
* `env.yml`: Conda environment specification for production parity.
