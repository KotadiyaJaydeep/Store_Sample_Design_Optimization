# sample_design_optimization.py
import os
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DATA_DIR = os.path.join(ROOT, 'data')
OUTPUT_DIR = os.path.join(ROOT, 'output')
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

pop_path = os.path.join(DATA_DIR, 'retail_population.csv')
if not os.path.exists(pop_path):
    np.random.seed(42)
    n_pop = 5000
    formats = ['Kirana','Modern Trade','Convenience','Wholesale']
    regions = ['North','South','East','West']
    pop = pd.DataFrame({
        'store_id': np.arange(1, n_pop+1),
        'format': np.random.choice(formats, size=n_pop),
        'region': np.random.choice(regions, size=n_pop),
        'monthly_sales': np.round(np.random.gamma(shape=2.0, scale=20000, size=n_pop)).astype(int)
    })
    pop.to_csv(pop_path, index=False)
else:
    pop = pd.read_csv(pop_path)

pop2 = pop.copy()
pop2['format_code'] = pop2['format'].map({'Kirana':0,'Modern Trade':1,'Convenience':2,'Wholesale':3})
features = pop2[['monthly_sales','format_code']].values
scaler = StandardScaler()
X = scaler.fit_transform(features)

k = 8
km = KMeans(n_clusters=k, random_state=42)
pop2['cluster'] = km.fit_predict(X)

total_sample = 1000
cluster_sizes = pop2.groupby('cluster')['store_id'].count().reset_index().rename(columns={'store_id':'size'})
cluster_sizes['alloc'] = (cluster_sizes['size']/cluster_sizes['size'].sum()*total_sample).round().astype(int)
cluster_sizes.loc[cluster_sizes['alloc'] < 5, 'alloc'] = 5

selected = []
for _, r in cluster_sizes.iterrows():
    c = r['cluster']
    n = int(r['alloc'])
    cluster_df = pop2[pop2['cluster']==c]
    n = min(n, len(cluster_df))
    s = cluster_df.sample(n=n, random_state=42)
    s = s.copy()
    s['cluster_alloc'] = r['alloc']
    selected.append(s)
selected_df = pd.concat(selected, ignore_index=True)
selected_df.to_csv(os.path.join(OUTPUT_DIR, 'selected_sample.csv'), index=False)

summary = selected_df.groupby('cluster').agg(
    selected_count=('store_id','count'),
    avg_sales_selected=('monthly_sales','mean')
).reset_index().merge(cluster_sizes[['cluster','size']], on='cluster', how='left')
summary.to_csv(os.path.join(OUTPUT_DIR, 'selection_summary.csv'), index=False)

print('Sample design optimization: selected sample and summary written.')
