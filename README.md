
# YouTube Analytics Data Engineering Project

This project demonstrates an end-to-end data engineering solution that ingests, transforms, and analyzes YouTube trending video statistics using AWS services. The final output is an interactive dashboard built with Amazon QuickSight to derive insights such as top-performing content categories, regional viewership trends, and user engagement metrics.

## Use Case

A streaming analytics team wants to analyze YouTube trending data to better understand what types of content perform well across different regions (US, GB, CA). Business stakeholders need KPIs such as most viewed content, regional user behavior, engagement rates (likes/comments), and daily view trends to make data-driven content and marketing decisions.

---

## Architecture Overview

**Data Source:**  
YouTube trending video statistics (CSV & JSON files) stored in Amazon S3.

**Pipeline Workflow:**
1. **Ingestion Layer:**
   - Raw CSV and JSON data uploaded to an S3 bucket.
   - AWS Lambda triggers on `ObjectCreated` events to initiate processing.

2. **Processing & Cleansing:**
   - AWS Glue ETL jobs read raw data and apply schema mapping.
   - Data is filtered (e.g., by region), cleaned, and transformed.
   - Output is written in partitioned Parquet format to the Cleansed S3 layer.

3. **Analytics Layer:**
   - Glue Crawlers catalog the cleansed data.
   - AWS Athena used for validation and query testing.
   - Amazon QuickSight connects to the Glue Data Catalog to build dashboards.

---

## Tools & Technologies

| Layer           | Tools/Services                                                                 |
|----------------|----------------------------------------------------------------------------------|
| Ingestion       | Amazon S3, AWS Lambda                                                          |
| Processing      | AWS Glue Studio, PySpark, Glue DynamicFrames                                   |
| Data Storage    | Amazon S3 (raw, cleansed, and analytics zones)                                 |
| Cataloging      | AWS Glue Crawlers, AWS Glue Data Catalog                                       |
| Query Engine    | Amazon Athena                                                                  |
| Visualization   | Amazon QuickSight                                                              |
| Orchestration   | AWS Lambda triggers + Glue ETL jobs                                            |
| Language        | Python (PySpark, AWS Glue Python SDK)                                          |

---

## Key Features

- Pushdown filtering for performance (`region in ('us','ca','gb')`)
- Schema mapping and type casting
- Data quality assurance (row count validation)
- Partitioned storage by `region` and `category_id`
- Interactive QuickSight dashboards with visual KPIs

---

## QuickSight Dashboard Visuals

**Metrics Tracked:**
- Total views, likes, and comments
- Top performing videos by views & likes
- Views by category and region
- Viewership trend over time
- Engagement by content type

> See `/screenshots` folder for visualizations.

---

## Folder Structure
📁 youtube-analytics-project/ ├── lambda/ # Lambda function for trigger-based ingestion ├── glue-jobs/ # ETL PySpark scripts for AWS Glue ├── scripts/ # Athena SQL or crawler setup scripts ├── screenshots/ # QuickSight visuals ├── README.md

