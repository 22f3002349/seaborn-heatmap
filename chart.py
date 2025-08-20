# chart.py
# Author: 22f3002349@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data: customer engagement (Hours of Day vs Days of Week)
np.random.seed(42)
hours = [f"{h}:00" for h in range(9, 21)]  # Business hours 9 AM - 8 PM
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Engagement scores (simulated)
data = np.random.randint(20, 100, size=(len(hours), len(days)))

# Create DataFrame
df = pd.DataFrame(data, index=hours, columns=days)

# Create heatmap
plt.figure(figsize=(8, 8))  # ensures 512x512 pixels when saved with dpi=64
ax = sns.heatmap(df, cmap="YlGnBu", annot=True, fmt="d", cbar_kws={"label": "Engagement Score"})

# Titles and labels
plt.title("Customer Engagement Heatmap", fontsize=16, pad=15)
ax.set_xlabel("Day of Week")
ax.set_ylabel("Hour of Day")

# Save as exactly 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
