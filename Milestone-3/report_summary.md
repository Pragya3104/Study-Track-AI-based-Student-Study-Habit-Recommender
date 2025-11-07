# Milestone 3: Recommendation Engine

## Objective
To use the cluster results from Milestone 2 to provide simple and useful recommendations for each group of customers.

## Dataset
Dataset used: customer_clusters.csv (contains the Cluster column)
Source: Created in Milestone 2 from merged customer and transaction data.

## Steps Followed
1. Loaded the dataset that included the Cluster column.
2. Observed the characteristics of each cluster.
3. Assigned a recommendation message to each cluster using a function.
4. Added a new column "Recommendation" to the dataset.
5. Added another column "Suggested_Tool" to provide a practical action.
6. Created a count plot showing how many customers fall under each recommendation.

## Tools Used
- Python
- Pandas
- Seaborn
- Matplotlib
- KMeans clustering (from Milestone 2)

## Key Insights
- Cluster 1 customers buy more and more often → They should be rewarded to maintain loyalty.
- Cluster 0 customers buy less → They may respond to discounts or special offers.
- Cluster 2 customers buy less frequently but spend higher per item → They may prefer premium product suggestions.

## Visualization
A count plot was created to show how many customers received each recommendation.
Saved as: visualizations/recommendation_countplot.png
