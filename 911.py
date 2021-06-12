#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
# %%
data = pd.read_csv("D:\\Python\\Phase 2\\Projects and Exerises\\Py-DS-ML-Bootcamp-master\\10-Data-Capstone-Projects\\911.csv")
# %%
# Basic data manupulation
# %%
data.info()
# %%
data.head()
# %%
data['zip'].value_counts().head()
# %%
data['twp'].value_counts().head()
# %%
data['title'].nunique()
# %%
# converting time stamp from string to date and time 
# %%
data['timeStamp'] = pd.to_datetime(data['timeStamp'])
# %%
# Adding a new colum called reason
# %%
data['Reason'] = data['title'].apply(lambda r:r.split(":")[0])
# %%
data.head()
# %%
data['Reason'].value_counts()
# %%
sns.countplot(data['Reason'])
plt.show()
# %%
## separating hours days and months from time stamps
# %%
data['Hour'] = data['timeStamp'].apply(lambda h: h.hour)
data.head()
# %%
data['Month'] = data['timeStamp'].apply(lambda m: m.month)
data.head()
# %%
data['Day of Week'] = data['timeStamp'].apply(lambda w: w.dayofweek)
data.head()
# %%
## changing the day of week to words
# %%
dict = {1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat', 7:'Sun'}
# %%
data['Day of Week'] = data['Day of Week'].map(dict)
# %%
data.head()
# %%
## ploting count plot for week and month
# %%
sns.countplot(data['Month'], hue=data["Reason"])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
# %%
sns.countplot(x='Day of Week', data= data, hue= "Reason",)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
# %%
data['Date'] = data['timeStamp'].apply(lambda d: d.date())
data['Date']
# %%
byDate = data.groupby("Date").count()
byDate.head()
# %%
byDate['twp'].plot()
plt.show()
# %%
byMonth = data.groupby("Month").count()
byMonth.head()
# %%
byMonth['twp'].plot()
plt.show()
# %%
data[data['Reason']== 'Traffic'].groupby("Date").count()['twp'].plot()
plt.title("Traffic vs Date")
plt.show()
# %%
data[data['Reason'] == 'Fire'].groupby("Date").count()['twp'].plot()
plt.title("Fire vs Date")
plt.show()
# %%
data[data['Reason'] == 'EMS'].groupby("Date").count()['twp'].plot()
plt.title("EMS vs Date")
plt.show()
# %%
## Cluster maps
# %%
dayHour = data.groupby(['Day of Week', 'Hour']).count()['Reason'].unstack()
dayHour.head()
# %%
plt.figure(figsize=(12,8))
sns.heatmap(dayHour, cmap="coolwarm")
plt.show()
# %%
plt.figure(figsize=(12,8))
sns.clustermap(dayHour, cmap="coolwarm")
plt.show()
# %%
dayMonth = data.groupby(['Month', 'Hour']).count()['Reason'].unstack()
dayMonth.head()
# %%
plt.figure(figsize=(12,8))
sns.heatmap(dayMonth, cmap="coolwarm")
plt.show()
# %%
plt.figure(figsize=(12,8))
sns.clustermap(dayMonth, cmap="coolwarm")
plt.show()