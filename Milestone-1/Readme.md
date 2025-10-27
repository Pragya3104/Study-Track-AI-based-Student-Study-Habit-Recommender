# Milestone 1 – Data Preprocessing and Exploratory Data Analysis

## Objective
The goal of this milestone is to perform data preprocessing and exploratory data analysis (EDA) to create a clean and analyzable dataset.  
The selected dataset focuses on an e-commerce theme and contains customer and transaction information.  
Both tables are related through a common key, `CustomerID`.



## Dataset Description
Two CSV files were used in this milestone:

1. **customers.csv** – Contains details about customers such as ID, location, and segment.  
2. **transactions.csv** – Contains order-level details including products, quantity, and total price.

These datasets are related by the **CustomerID** column.

**Source:** Public e-commerce dataset (Kaggle)  
**Modified:** Split into two tables for analysis – `customers` and `transactions`.


##  Steps Followed

### 1. Data Preparation
- Loaded both CSV files using pandas.  
- Merged them using the common key `CustomerID` with an inner join.  

### 2. Data Preprocessing
- Checked and handled missing values.  
- Removed duplicate entries.  
- Corrected data types where needed.  
- Encoded categorical columns using label encoding.  
- Scaled numerical columns where appropriate.

### 3. Descriptive Analysis
- Computed summary statistics (mean, median, std, correlations).  
- Identified outliers and possible imbalances in numerical data.  

### 4. Exploratory Data Analysis (EDA)
- Visualized distributions of sales and quantities.  
- Compared product categories and customer segments using bar plots.  
- Created scatter plots to study relationships between key variables.  
- Generated a correlation heatmap to understand feature relationships.  
- Analyzed patterns and trends over time.


##  Tools and Libraries Used
- **Python** (Jupyter Notebook)  
- **Pandas** – Data handling and preprocessing  
- **Matplotlib** & **Seaborn** – Visualizations  


## Key Insights
- Most customers are concentrated in a few regions, indicating focused sales areas.  
- Product quantities and sales values show a positive correlation.  
- Certain products have significantly higher average prices, possibly due to category differences.  
- Outliers in transaction amounts suggest bulk or special orders.  

