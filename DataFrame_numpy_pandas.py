#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing python library
import pandas as pd
import numpy as np


# In[3]:


data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame=pd.DataFrame(data)
#using the jupyter notebook,pandas dataframe objects will be displayed as a more browser friendly HTML table.
frame


# In[4]:


#head method selects only first five rows
frame.head()


# In[5]:


#specify a sequence of columns
pd.DataFrame(data,columns=['year','state','pop'])


# In[6]:


frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
frame2


# In[7]:


frame2.columns


# In[8]:


#A column in a DataFrame can be retrieved as a series either by dict-like notation or by attribute
frame2['state']


# In[9]:


frame2.year


# In[10]:


#Rows can be retrieved by position or name with the special loc attribute
frame2.loc['three']


# In[11]:


#columns can be modified by assignment
#'debt' column could be assigned a scalar value or an array of values
frame2['debt']=16.5
frame2


# In[12]:


frame2['debt']=np.arange(6.)
frame2


# In[14]:


#assign a series,its labels will be realignes exactly to the Dataframes index,inserting missing values in any values in any holes
val=pd.Series([-1.2,-1.5,1.7],index=['two','four','five'])
frame2['debt']=val
frame2


# In[15]:


frame2['eastern']=frame2.state=='Ohio'
frame2


# In[16]:


del frame2['eastern']
frame2.columns


# In[17]:


pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=pd.DataFrame(pop)
frame3


# In[18]:


frame3.T


# In[19]:


pd.DataFrame(pop,index=[2002,2002,2003])


# In[20]:


frame3.index.name='year';frame3.columns.name='state'
frame3


# In[21]:


frame3.values


# In[22]:


frame2.values


# In[ ]:




