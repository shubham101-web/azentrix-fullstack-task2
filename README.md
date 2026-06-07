# Mini Data Lakehouse with Analytics Dashboard

A complete ETL (Extract, Transform, Load) pipeline that ingests data from CSV and REST API sources, transforms and cleans the data, stores curated datasets, loads analytics-ready data into PostgreSQL, and visualizes insights through an interactive Streamlit dashboard.

---

## Project Overview

This project implements a Mini Data Lakehouse architecture that:

* Extracts data from CSV and REST API sources
* Cleans and transforms raw datasets
* Generates curated analytics datasets
* Loads processed data into PostgreSQL
* Visualizes insights using Streamlit
* Supports Docker-based deployment

---

## Features

* CSV Data Ingestion
* REST API Data Ingestion
* Data Cleaning & Transformation
* Curated Analytics Dataset Generation
* PostgreSQL Analytics Layer
* Interactive Streamlit Dashboard
* Dockerized Deployment
* Modular ETL Pipeline

---

## Project Structure

```text
azentrix-fullstack-task2/
│
├── dashboard/
│   └── app.py
│
├── pipeline/
│   ├── ingest.py
│   ├── transform.py
│   ├── load.py
│   └── run_pipeline.py
│
├── sql/
│   └── schema.sql
│
├── data/
│
├── screenshots/
│   ├── project-structure.png
│   ├── etl-ingestion.png
│   ├── etl-transformation.png
│   ├── dashboard-home.png
│   ├── revenue-trend.png
│   └── top-products.png
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Technology Stack

### Programming

* Python

### Data Processing

* Pandas
* Requests
* PyArrow

### Database

* PostgreSQL
* SQLAlchemy

### Visualization

* Streamlit
* Plotly

### Containerization

* Docker
* Docker Compose

---

## ETL Workflow

### 1. Extract

* Read source data from CSV files
* Fetch additional data from REST APIs

### 2. Transform

* Clean and validate records
* Handle missing values
* Standardize formats
* Generate analytics-ready datasets

### 3. Load

* Load transformed datasets into PostgreSQL tables

### 4. Visualize

* Display business insights using Streamlit dashboards

---

## Screenshots

### Project Structure

![Project Structure](screenshots/project-structure.png)

### ETL Ingestion

![ETL Ingestion](screenshots/etl-ingestion.png)

### Data Transformation

![ETL Transformation](screenshots/etl-transformation.png)

### Dashboard Home

![Dashboard Home](screenshots/dashboard-home.png)

### Revenue Trend Analysis

![Revenue Trend](screenshots/revenue-trend.png)

### Top Products Analysis

![Top Products](screenshots/top-products.png)

---

## Local Setup

### Clone Repository

```bash
git clone <repository-url>
cd azentrix-fullstack-task2
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## PostgreSQL Configuration

Ensure PostgreSQL is running locally on:

```text
localhost:5432
```

Default database connection:

```text
postgresql://postgres:postgres@localhost:5432/lakehouse
```

---

## Run ETL Pipeline

### Ingestion

```bash
python pipeline/ingest.py
```

### Transformation

```bash
python pipeline/transform.py
```

### Load into PostgreSQL

```bash
python pipeline/load.py
```

Expected Output:

```text
Loaded
```

---

## Run Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

## Docker Deployment

Start containers:

```bash
docker-compose up --build
```

Stop containers:

```bash
docker-compose down
```

---

## GitHub Repository

GitHub repository link will be added before final submission.

---

## Loom Demonstration Video

Loom video link will be added after recording and uploading the project demonstration.

---

## Submission Checklist

* ETL Pipeline Implemented
* PostgreSQL Integration
* Streamlit Dashboard
* Docker Support
* Screenshots Included
* Documentation Completed
* GitHub Repository Added
* Loom Video Added

---

## Author

Shubham

Project: Azentrix Full Stack Task 2


