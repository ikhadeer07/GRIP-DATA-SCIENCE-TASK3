# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('SampleSuperstore.csv')

# Check the structure of the data
print(data.head())
print(data.describe())
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Check for duplicates
print(data.duplicated().sum())

# Visualize the data
sns.pairplot(data)
plt.show()

sns.heatmap(data.corr(), cmap='coolwarm')
plt.show()

sns.boxplot(data['variable'], orient='v')
plt.show()

# Perform statistical analysis
corr = data.corr()
print(corr)

# Identify weak areas and business problems
# Based on the EDA, you can identify areas where the business is underperforming and potential problems that may affect profit. For example, if the sales are declining in a particular product category or region, it may indicate weak areas that need improvement. Similarly, if there are issues with inventory management or pricing strategies, it may affect the profit margins.

# Formulate strategies to address the problems
# Based on the insights gained, formulate strategies to address the weak areas and business problems. For example, you may need to improve the quality of the product or service, optimize pricing strategies, or focus on marketing and promotions to increase sales.

