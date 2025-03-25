# 🎬 YouTube Analytics Data Engineering Project

An end-to-end data engineering pipeline built on AWS that ingests, transforms, and analyzes YouTube trending video statistics. The final output is a fully interactive dashboard in **Amazon QuickSight** showcasing insights like top-performing categories, regional viewership patterns, and audience engagement metrics.

---

## 📌 Use Case

A data team at a media analytics company needs to monitor global YouTube trends to help content strategists, marketers, and executives understand:

- Which **types of content** perform best across different **regions** (US, GB, CA)?
- How do **views, likes, and comments** vary over time?
- What are the most **engaging videos and categories**?

This project simulates that real-world scenario by building a complete data pipeline and BI dashboard to support those insights.

---

## 🧩 Architecture Overview

**🗂️ Data Source:**  
Raw CSV and JSON files containing YouTube video metadata (views, likes, category, etc.) stored in Amazon S3.

**⚙️ Pipeline Components:**

1. **Ingestion Layer**
   - Raw data files uploaded to `s3://de-on-youtube-raw-*`
   - AWS Lambda triggers on `ObjectCreated` events

2. **Processing & Cleansing**
   - AWS Glue ETL jobs transform and filter data
   - Data is cleaned, typed, deduplicated, and converted to **Parquet**
   - Output stored in partitioned form in a Cleansed S3 bucket

3. **Analytics & Visualization**
   - AWS Glue Crawlers catalog data into the Data Catalog
   - Athena used for exploratory SQL queries
   - QuickSight connected to the cleansed catalog table for visual dashboards

---

## 🛠️ Tools & Technologies

| Layer            | Services & Tools                                                                 |
|------------------|----------------------------------------------------------------------------------|
| Ingestion        | **Amazon S3**, **AWS Lambda**                                                    |
| Processing       | **AWS Glue Studio**, **PySpark**, **Glue DynamicFrame API**                      |
| Data Storage     | Amazon S3 (Raw, Cleansed, Analytics)                                             |
| Cataloging       | AWS Glue Crawlers, Glue Data Catalog                                             |
| Query Engine     | **Amazon Athena**                                                                |
| Visualization    | **Amazon QuickSight**                                                            |
| Language         | **Python**, PySpark (for Glue), SQL (for Athena)                                 |
| Orchestration    | Event-based triggers (S3 → Lambda → Glue)                                        |

---

## 🔍 Key Features

- Predicate pushdown filtering (`region in ('us', 'ca', 'gb')`) for performance
- Schema mapping and data type casting
- Data Quality validation (row counts, column integrity)
- Partitioned data lake by `region` and `category_id`
- KPI cards, category trends, and regional breakdowns in QuickSight

---

## 📊 QuickSight Dashboard Insights

**Metrics & Visuals Tracked:**

- ✅ Total Views, Likes, Comments (KPI Cards)
- 📈 Views over Time (Line Chart)
- 🌍 Viewership Share by Region (Donut Chart)
- 🎵 Most Viewed Content Categories (Bar Chart)
- 👍 Top Performing Videos by Likes & Views (Table)
- 💬 Engagement by Category (Likes, Comments)

> You can find these charts in the `/screenshots` folder or explore them directly in QuickSight if connected.

---


## 🧠 Skills Demonstrated

- Cloud-native ETL using **AWS Glue**
- Trigger-based data movement via **AWS Lambda**
- Working with **partitioned data lakes** using Parquet
- Data modeling with **PySpark + Glue DynamicFrames**
- Querying and validation with **Athena**
- Business storytelling and dashboard design in **QuickSight**
- Professional project documentation using **GitHub**

---
