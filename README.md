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
python Retail_Sales_Universe_Estimation/notebooks/universe_estimation.py
python Store_Sample_Design_Optimization/notebooks/sample_design_optimization.py
python Retail_Index_Construction_and_Monitoring/notebooks/retail_index.py
```

### 3️⃣ Generate Dashboard Plots (PNG outputs)  
```bash
python Retail_Sales_Universe_Estimation/plots/plot_stratum_counts.py
python Retail_Sales_Universe_Estimation/plots/plot_sales_distribution.py
python Store_Sample_Design_Optimization/plots/plot_cluster_counts.py
python Store_Sample_Design_Optimization/plots/plot_selected_vs_pop_sales.py
python Retail_Index_Construction_and_Monitoring/plots/plot_index_timeseries.py
python Retail_Index_Construction_and_Monitoring/plots/plot_index_pct_change.py
```

---

## 📊 Power BI Dashboard Instructions  

### A) **Retail Sales Universe Estimation — Validation Dashboard**  
- Files:  
  - `data/retail_population.csv`  
  - `output/stratified_sample.csv`  
  - `output/estimation_results.csv`  

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
  - `output/selected_sample.csv`  
  - `output/selection_summary.csv`  

**Suggested visuals:**  
- Bar chart: Selected count by cluster  
- Histogram: Sales distribution (population vs. sample)  
- Scatter plot: Monthly sales vs. store ID (colored by cluster)  
- Matrix table: Cluster sizes, selected counts, avg sales  
- Bookmarks: Before vs. After sample selection  

---

### C) **Retail Index Construction & Monitoring — Index Dashboard**  
- Files:  
  - `output/index_timeseries.csv`  
  - `data/price_samples.csv`  

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
import plotly.express as px

df = pd.read_csv('Retail_Index_Construction_and_Monitoring/output/index_timeseries.csv')
fig = px.line(df, x='month', y='index_smooth', title='Retail Price Index (Smoothed)')
fig.write_image('index_plot.png')  # requires `pip install plotly kaleido`
```

---

## ✅ Summary  

This repository demonstrates a **full workflow** of:  
- Sampling and estimation  
- Sample design optimization  
- Index construction and anomaly detection  
- Dashboarding in Power BI  

It serves as a **hands-on portfolio project** for retail analytics and monitoring.  
