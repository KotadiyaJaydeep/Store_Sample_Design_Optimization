# plot_cluster_counts.py
import os, pandas as pd, matplotlib.pyplot as plt
HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..'))
DATA_DIR = os.path.join(ROOT, 'data')
OUTPUT_DIR = os.path.join(ROOT, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Use selected sample or pop
sel = pd.read_csv(os.path.join(OUTPUT_DIR, 'selected_sample.csv')) if os.path.exists(os.path.join(OUTPUT_DIR, 'selected_sample.csv')) else None
pop = pd.read_csv(os.path.join(DATA_DIR, 'retail_population.csv'))

if sel is not None:
    counts = sel['cluster'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8,6))
    counts.plot(kind='bar', ax=ax)
    ax.set_title('Selected Sample Count by Cluster')
    ax.set_xlabel('Cluster')
    ax.set_ylabel('Count')
    plt.tight_layout()
    out = os.path.join(OUTPUT_DIR, 'selected_cluster_counts.png')
    fig.savefig(out)
    plt.close(fig)
    print('Wrote', out)
else:
    print('selected_sample.csv missing; run sample_design_optimization.py first')
