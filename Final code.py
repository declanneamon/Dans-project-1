#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import requests
import matplotlib.pyplot as plt

# Fetch data from the FEMA API
api_url = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    disasters = data.get('DisasterDeclarationsSummaries', [])
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
    disasters = []

# Create a DataFrame from the fetched data
df = pd.DataFrame(disasters)

# Check if the DataFrame is not empty before creating the heatmap
if not df.empty:
    # Create a pivot table for better heatmap representation
    heatmap_data = df.pivot_table(index='fipsCountyCode', columns='incidentType', aggfunc='size', fill_value=0)

    # heatmap using seaborn
    plt.figure(figsize=(15, 60))
    sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt='g', cbar_kws={'label': 'Number of Incidents'})
    plt.title('Natural Disasters Heatmap in the USA')
    plt.show()
else:
    print("No data available to create the heatmap.")


# In[6]:


df.head (50)


# In[ ]:





# ### 
