# plot_selected_vs_pop_sales.py
import os, pandas as pd, matplotlib.pyplot as plt
HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DATA_DIR = os.path.join(ROOT, 'data')
OUTPUT_DIR = os.path.join(ROOT, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

pop = pd.read_csv(os.path.join(DATA_DIR, 'retail_population.csv'))
sel = pd.read_csv(os.path.join(OUTPUT_DIR, 'selected_sample.csv')) if os.path.exists(os.path.join(OUTPUT_DIR, 'selected_sample.csv')) else None

fig, ax = plt.subplots(figsize=(8,6))
pop['monthly_sales'].hist(bins=50, alpha=0.7, ax=ax)
if sel is not None:
    sel['monthly_sales'].hist(bins=50, alpha=0.7, ax=ax)
ax.set_title('Population vs Selected Sample - Monthly Sales (overlaid)')
ax.set_xlabel('Monthly Sales')
ax.set_ylabel('Count')
plt.tight_layout()
out = os.path.join(OUTPUT_DIR, 'pop_vs_selected_sales.png')
fig.savefig(out)
plt.close(fig)
print('Wrote', out)
