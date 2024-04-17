#!/usr/bin/env python
# coding: utf-8

# In[6]:


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
    
    
    
    
   
#  data from the FEMA API
api_url = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    disasters = data.get('DisasterDeclarationsSummaries', [])
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
    disasters = []

# makes a DataFrame from the fetched data
df = pd.DataFrame(disasters)

# Check if the DataFrame is not empty before creating the bar chart
if not df.empty:
    # Count the occurrences of each incident type
    incident_counts = df['incidentType'].value_counts()

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x=incident_counts.index, y=incident_counts.values, palette='viridis')
    plt.title('Frequency of Natural Disasters')
    plt.xlabel('Incident Type')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()
else:
    print("No data available to create the bar chart.")
    
    
    
    
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

# Check if the DataFrame is not empty before creating the stacked area chart
if not df.empty:
    # Count the occurrences of each incident type for each county
    incidents_by_county = df.groupby(['state', 'incidentType']).size().unstack(fill_value=0)

    # Plot the stacked area chart
    plt.figure(figsize=(200, 100))  # Larger figure size
    incidents_by_county.plot(kind='area', stacked=True, cmap='viridis')
    plt.title('Stacked Area Chart of Natural Disasters by County')
    plt.xlabel('County')
    plt.ylabel('Number of Incidents')
    plt.legend(title='Incident Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
else:
    print("No data available to create the stacked area chart.")


# In[6]:


df.head (50)


# In[ ]:





# In[ ]:




