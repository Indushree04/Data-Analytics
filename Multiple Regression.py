#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt


# In[2]:


df1=pd.read_excel('D:/Indushree/TRUCKING.xlsx')
df1


# In[3]:


import matplotlib.pyplot as plt
plt.scatter(df1['x1'],df1['travel_time'],color="green")
plt.ylabel('travel time')
plt.title('Simple linear Regression with Miles travelled')


# In[4]:


plt.scatter(df1['n_of_deliveries'],df1['travel_time'],color="red")
plt.ylabel('Travel time')
plt.title('Simple linear Regression with number of Delivers')


# In[6]:


import matplotlib.pyplot as plt
plt.figure()
plt.scatter(df1['x1'],df1['travel_time'],color="green")
plt.scatter(df1['n_of_deliveries'],df1['travel_time'],color="red")
plt.ylabel('Travel time')
plt.title('Multiple Regression')
plt.xlabel('x1 in green and x2 in red')


# In[7]:


Reg1=ols(formula="travel_time~x1",data=df1)
Fit1=Reg1.fit()
print(Fit1.summary())


# In[9]:


from statsmodels.formula.api import ols
model=ols('travel_time~x1+n_of_deliveries',data=df1).fit()
model.summary()


# In[10]:


print(anova_lm(Fit1))


# In[11]:


anova_table=anova_lm(model,typ=1)
anova_table


# In[ ]:




