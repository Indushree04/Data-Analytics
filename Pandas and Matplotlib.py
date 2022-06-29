#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[5]:


#load the dataset
data1=pd.read_csv('D:\Indushree\gapminder_full.csv')


# In[6]:


#display dataset
data1


# In[7]:


#display the head of the dataset(show only 5 rows)
data1.head()


# In[8]:


#get number of rows and columns
print(data1.shape)


# In[9]:


#get column names
data1.columns


# In[10]:


#get the datatype of each column
data1.dtypes


# In[11]:


#get more info about data
data1.info()


# In[12]:


#looking at columns,rows and cells
#get the country column and save it in a new variable
country_data=data1['country']
#show the first 5 observation
country_data.head()


# In[13]:


#Show last 5 observation
country_data.tail()


# In[19]:


#looking at country,continent and year
subset=data1[['country','continent','year']]
subset.head()


# In[17]:


subset.tail()


# In[20]:


#Analytical summary of dataset
data1.describe(include='all')


# In[21]:


#histogram of all the variables in the dataset
data1.hist(figsize=(10,5))


# In[25]:


#Relationship between catagorical and continuous variable
sns.boxplot(x="year",y="life_exp",data=data1)


# In[26]:


#Drop irrelavant columns
data1=data1.drop(['year'],axis='columns')
data1.head(5)


# In[27]:


#Renaming the column name
data1=data1.rename(columns={"country":"countries"})
data1.head(5)


# In[32]:


#Rows containg duplicate data
duplicate_rows=data1[data1.duplicated()]
print("Number of duplicate rows",duplicate_rows.shape)


# In[30]:


#count the rows before moving the data
data1.count()


# In[ ]:




