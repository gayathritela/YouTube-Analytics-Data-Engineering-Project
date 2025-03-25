# YouTube Analytics Data Engineering Project

This project demonstrates a complete end-to-end data engineering pipeline on AWS using trending YouTube video data from Kaggle. The final result is a business-ready QuickSight dashboard to help stakeholders make data-driven decisions.

---

## 🎯 Project Overview
This project simulates a real-world scenario where a video streaming analytics team wants to:
- Understand what type of content performs well across regions (US, GB, CA)
- Track daily video performance trends
- Identify top performing creators and categories
- Measure user engagement through views, likes, and comments

The dataset used is from Kaggle's [Trending YouTube Video Statistics](https://www.kaggle.com/datasets/datasnaek/youtube-new).

---

## ✅ Project Goals
- **Data Ingestion**: Automatically ingest CSV and JSON files into AWS S3 (raw layer)
- **ETL System**: Clean and transform raw data using AWS Glue (PySpark)
- **Data Lake Formation**: Store data in partitioned Parquet format (cleansed layer)
- **Scalability**: Use serverless services like Glue, Lambda, and S3 for handling scale
- **Cloud-Native Architecture**: Entirely built and deployed on AWS
- **Reporting**: Deliver insights through an interactive Amazon QuickSight dashboard

---

## 🏗️ Architecture

The pipeline follows a modular and scalable architecture leveraging AWS Glue, Lambda, S3, Athena, and QuickSight.

![Architecture Diagram](architecture.jpeg)

### Data Source
- YouTube trending video statistics (CSV files per region + JSON metadata)
- Dataset hosted on [Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new)

### AWS Services Used
| Layer             | Tools/Services                                                  |
|------------------|-----------------------------------------------------------------|
| Ingestion         | Amazon S3, AWS Lambda                                           |
| Processing        | AWS Glue Studio, PySpark, Glue DynamicFrames                    |
| Data Storage      | Amazon S3 (raw, cleansed, analytics zones)                      |
| Cataloging        | AWS Glue Crawler, AWS Glue Data Catalog                         |
| Query Engine      | Amazon Athena                                                   |
| Visualization     | Amazon QuickSight                                               |
| Orchestration     | AWS Lambda (event triggers), Glue Workflows                     |
| Permissions       | AWS IAM (roles for S3, Glue, Athena, QuickSight)                |

---

## 📊 QuickSight Dashboard Highlights
- **KPIs (KPI Cards)**:
  - Total Views, Likes, Comments
  - Number of Active Regions

- **Bar & Donut Charts**:
  - Top Content Categories by Views
  - Regional Viewership Distribution
  - Count of Likes by Content Type

- **Time-Series Line Graph**:
  - Daily Trends in Views Over Time

- **Table View**:
  - Top Performing Videos by Likes and Views

---

## 📁 Folder Structure
```
youtube-analytics-project/
├── lambda/                  # Lambda function code for S3 trigger events
├── glue-jobs/               # ETL jobs (PySpark scripts)
├── scripts/                 # Athena SQL queries, Glue crawler configs
├── screenshots/             # Sample QuickSight dashboard images
├── README.md                # Project documentation
```

---

## 🚀 Skills & Concepts Demonstrated
- Cloud Data Engineering (AWS-first approach)
- Serverless ETL development with AWS Glue
- Event-driven processing using AWS Lambda
- Partitioned data lake architecture on S3
- Query optimization with Athena + Parquet
- Business intelligence and storytelling via QuickSight
- End-to-end project structuring and GitHub documentation

---

## 📦 Dataset Source
**Trending YouTube Video Statistics** – [Kaggle Link](https://www.kaggle.com/datasets/datasnaek/youtube-new)
- Daily trending video data per region (US, GB, CA)
- Includes fields like: `video_id`, `title`, `category_id`, `views`, `likes`, `comments`, `publish_time`, etc.
- Category metadata provided via JSON files

---

## 📸 Dashboards
> 📍Screenshots are available in the `screenshots/` folder. 
> Final QuickSight visuals show KPIs, time trends, category performance, and regional breakdowns.

---



