# Milestone 2 — Clustering and Pattern Detection

## Objective
To cluster customers based on transactional behavior using K-Means and analyze spending patterns through visual interpretation.

## Dataset Source
Dataset: `merged_customer_data.csv` — merged customer demographic and transaction data.

## Steps Followed
- **Join:** Combined customer and transaction tables.
- **Clean:** Removed null values and selected relevant numerical features.
- **Visualize:** Explored correlations and feature distributions.
- **Prepare:** Standardized data using `StandardScaler`, applied PCA for 2D visualization.
- **Cluster:** Used K-Means, found optimal `k=3` using the Elbow Method.
- **Analyze:** Assigned cluster labels, summarized metrics, and visualized results.

## Tools Used
Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn) — executed on Google Colab.

## Key Insights and Observations
- The **Elbow Method** plot showed the bend at `k=3`, confirming 3 distinct customer segments.
- The **PCA Scatter Plot** displayed clear cluster separation, indicating strong differentiation in behavior.
- The **Cluster Profile Bar Chart** revealed that Cluster 0 had the highest average transaction value and frequency.
- The **Box Plots** showed spending variability across clusters, where Cluster 2 customers had more consistent but lower transactions.
- The **Cluster Size Distribution** plot indicated most customers fall under moderate spending behavior (Cluster 1).
- Overall, clusters represent **high-value**, **average**, and **low-activity** customer groups — helpful for marketing and engagement strategies.
