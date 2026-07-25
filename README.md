# Retail Business Performance Analysis

## Project Overview

This project analyzes customer transaction data from a retail business operating in multiple shopping malls. The goal was to identify key revenue drivers and provide management with a clear, data‑driven view of business performance.

**Key Question:**  
*Which product categories, shopping malls, and customer segments generate the most revenue?*

## Problem Statement

Management lacked a unified view of their business performance. They had transaction data but no easy way to answer basic questions like:  
- Which product categories bring in the most revenue?  
- Which shopping malls perform best?  
- Who are our most valuable customers?

Without these insights, decisions about marketing, inventory, and mall operations were being made based on intuition rather than data.

## Approach

I followed a standard data analysis pipeline:

1. **Load & Explore** – Loaded the data and checked for missing values, duplicates, and data types.  
2. **Clean** – Removed one row with missing data. Since only 1 row out of 504 was affected, dropping it was the safest and most honest approach.  
3. **Calculate Key Metrics** – Total revenue, average order value, top categories, top malls, and customer counts.  
4. **Visualize** – Created bar charts and a histogram to show revenue distribution and customer age patterns.  
5. **Export Reports** – Saved results to Excel for further exploration and generated a PDF summary for management.

**Tools Used:**  
Python, Pandas, Matplotlib, FPDF, OpenPyXL


## Solution

I built a Python script that automates the entire analysis. Running the script produces:

- A clean Excel file (`retail_report.xlsx`) with:
  - Raw data
  - Revenue by product category
  - Revenue by shopping mall
  - Summary metrics
- A PDF report (`retail_summary.pdf`) with key metrics and charts
- PNG charts saved in a `charts/` folder


## Key Findings

| Metric                 Value 
| **Total Revenue**     $1,831,758.88
| **Average Order Value**  $3,641.67 
| **Total Customers**    371 
| **Total Transactions**   504 
| **Top Product Category** Clothing 
| **Top Shopping Mall**    Metrocity 


## Recommendations

1. **Focus marketing on Clothing and Technology** – these are the top revenue categories.  
2. **Prioritize Metrocity** – it is the best‑performing mall. Invest in events and promotions there.  
3. **Target the 25–35 age group** – they represent the largest customer segment. Consider loyalty programs or targeted campaigns.
## Files in This Repository

| File                  Description |
| `retail_analysis.py`  Main Python script |
| `retail_report.xlsx`  Excel report with data and summaries |
| `retail_summary.pdf`  One‑page PDF summary for management |
| `charts/`             Folder containing all visualizations (PNG) |
| `shopping_trends.csv` Original dataset |


## About the Data

The dataset contains 504 transactions from a retail business. It includes customer demographics, product categories, quantities, prices, payment methods, and shopping mall locations.

## Author

Tatah Clevis – Data Analyst  
[GitHub](https://github.com/NGAI-5) | [LinkedIn](https://linkedin.com/in/tatahclevis)