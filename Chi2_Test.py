#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


acad=pd.read_excel('D:/Indushree/acad.xlsx')


# In[3]:


acad


# In[4]:


obs=pd.pivot_table(acad[['g','sm']],index='g',columns='sm',aggfunc=len)
obs


# In[5]:


from scipy.stats import chi2_contingency


# In[6]:


chi2,p,dof,tbl=chi2_contingency(obs)


# In[7]:


chi2


# In[8]:


p


# In[9]:


dof


# In[10]:


tbl


# In[11]:


import scipy
from scipy.stats import chi2
from scipy.stats import poisson


# In[12]:


import pandas as pd
import numpy as np


# In[13]:


data=pd.read_excel('D:/Indushree/p_distribution.xlsx')
data


# In[14]:


observed_Freq=data['Frequency']


# In[15]:


observed_Freq


# In[16]:


total_arrival=600
total_time_period=100
mu=total_arrival/total_time_period


# In[17]:


mu


# In[18]:


Expected_Freq=[]
for i in range(len(observed_Freq)):
    E_Freq=100*poisson.pmf(i,mu)
    Expected_Freq.append(E_Freq)


# In[19]:


Expected_Freq


# In[20]:


Expected_Freq_round_off=[round(elem,2) for elem in Expected_Freq]
Expected_Freq_round_off


# In[21]:


df=pd.DataFrame(list(zip(observed_Freq,Expected_Freq_round_off)),columns=['observed Frequency','Expected Frequency'])
df


# In[30]:


obs_freq=[5,10,14,20,12,12,9,8,10]
expected_freq=[6.20,8.92,13.39,16.06,16.06,13.77,10.33,6.88,8.39]


# In[31]:


scipy.stats.chisquare(obs_freq,expected_freq)


# In[ ]:





# In[ ]:




