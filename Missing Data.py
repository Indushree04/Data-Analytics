#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
df=pd.read_csv("D:\Indushree\emp.csv")
print(df.head())


# In[3]:


print(df.dtypes)
print(df.describe())


# In[4]:


print('Salary')
print(df['Salary'].head(10))


# In[5]:


print(df['Gender'].head(10))


# In[6]:


missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df=pd.read_csv("D:\Indushree\emp.csv",na_values=missing_value_formats)
print(df['Gender'].head(10))


# In[13]:


import pandas as pd
missing_value_formats=["n.a.","?","NA","n/a","na","--"]
df=pd.read_csv("D:\Indushree\emp.csv",na_values=missing_value_formats)
def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan
df['Salary']=df['Salary'].map(make_int)
print(df['Salary'].head())


# In[11]:


print(df['Gender'].isnull().head(10))
print(df['Gender'].notnull().head(10))


# In[12]:


null_filter=df['Gender'].notnull()
print(df[null_filter].head())


# In[14]:


print(df.isnull().values.any())


# In[15]:


print(df.isnull().sum())


# In[16]:


new_df=df.dropna(axis=0)
print(new_df.isnull().values.any())


# In[35]:


new_df=df.dropna(axis=0,how='any')
new_df


# In[30]:


new_df=df.dropna(axis=0,how='all')
new_df


# In[33]:



new_df=df.dropna(axis=1,how='any')
new_df


# In[34]:


new_df=df.dropna(axis=1,how='all')
new_df


# In[20]:


df['Salary'].fillna(0)


# In[21]:


df['Gender'].fillna('No Gender')


# In[22]:


df['Salary'].fillna(method='pad')


# In[23]:


df['Salary'].fillna(method='bfill')


# In[25]:


df['Salary'].fillna(int(df['Salary'].median()))


# In[24]:


df['Salary'].fillna(int(df['Salary'].mean()))


# In[27]:


df['Salary'].replace(to_replace=np.nan,value=0)


# In[28]:


df['Salary'].interpolate(method='linear',direction='forward')


# In[ ]:




