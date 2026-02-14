# 25280028
# Rubina Noor

Digital Health Data Engineering Pipeline

Overview

This project implements an ELT (Extract, Load, Transform) Data Engineering Pipeline focused on digital health data. The pipeline integrates multiple heterogeneous data sources:

-- Public API data (HealthData.gov / CDC)
-- Local structured dataset (CSV) downloaded from Kaggle
-- Google Trends time-series data

The goal is to extract, store, clean, transform, and analyze the data in preparation for downstream analytics.

Pipeline Architecture

The pipeline follows this structure:
Config → Extract → Raw Storage → Transform & Clean → Cleaned Storage → Analysis & Visualization

DE Assignment 1/
│
├── Part1_extraction.py
├── load.py
├── trends.py
├── run_pipeline.py
├── Part2_analysis.ipynb
├── config.json
│
├── data/
│   ├── raw/
│   │   ├── healthdata_raw.csv
│   │   ├── google_trends_raw.csv
│   │   ├── disease_diagnosis.csv
│   │   └── *.json
│   │
│   └── cleaned/
│       ├── extracted_api_cleaned_data.csv
│       ├── loaded_data_cleaned_data.csv
│       └── google_data_cleaned.csv
│
├── api_response_count_plot.png
├── trends_time_series_chart.png
├── loaded_data_box_plot.png
└── venv/


How to Run the Pipeline
1️ Activate Virtual Environment
source venv/bin/activate   # for Mac/Linux

2️ Install Dependencies
pip install pandas, matplotlib, seaborn, pytrends, requests, python3

3️ Run Orchestration File
python run_pipeline.py

4️ Run Analysis
Open Part2_analysis.ipynb