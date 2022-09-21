#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mlxtend


# In[2]:


import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori,association_rules


# In[3]:


df=pd.read_csv('D:/Indushree/GroceryStoreDataSet.csv',names=['products'],sep=',')
df.head()


# In[4]:


df.shape


# In[5]:


data=list(df["products"].apply(lambda x:x.split(",") ))
data


# In[6]:


from mlxtend.preprocessing import TransactionEncoder
a=TransactionEncoder()
a_data=a.fit(data).transform(data)
df=pd.DataFrame(a_data,columns=a.columns_)
df=df.replace(False,0)
df


# In[7]:


df=apriori(df,min_support=0.2,use_colnames=True,verbose=1)
df


# In[8]:


df_ar=association_rules(df,metric="confidence",min_threshold=0.6)
df_ar


# In[ ]:




