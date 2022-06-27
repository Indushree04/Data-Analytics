#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
#Create 1D array
arr1=np.array([1,2,3])
print(arr1)


# In[14]:


#accessing elements from array
arr1[2]


# In[3]:


#change an element from array
arr1[2]=5


# In[4]:


arr1


# In[15]:


#create 2D array
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)


# In[16]:


#check the shape of array
print("The Shape is 2 rows and 3 columns:",arr2.shape)


# In[17]:


#Accessing the elements from array
print(arr2[0][2])
print(arr2[0,2])
print(arr2[0,-1])
print(arr2[-1,0])


# In[18]:


#array of tye string
arr3=np.array(['India','China','USA','Mexico'])
print(arr3)


# In[10]:


arr3[1]


# In[19]:


#Array of evenly spaced values within specified interval
arr=np.arange(0,20,2)
print(arr)


# In[20]:


#Array of evenly spaced number in specified interval
arr=np.linspace(0,10,20)
print(arr)


# In[21]:


#Array of random values between 0 and 1 in a given shape
arr=np.random.rand(10)
print(arr)
print('\n')
arr=np.random.rand(3,4)
print(arr)


# In[22]:


#Array of constant values in a given shape
print(np.full((4,6),10))


# In[23]:


#Create an array by repitition
#repeat each element of an array by a specified number of times
arr=[0,1,2]
print(np.repeat(arr,3))


# In[24]:


#Repeat an array by a specified number of times
arr=[0,1,2]
print(np.tile(arr,3))


# In[26]:


#Create an identity matrix with eye
identity_matrix=np.eye(3)
print(identity_matrix)


# In[27]:


#Create an identity matrix with identity
identity_matrix=np.identity(3)
print(identity_matrix)


# In[28]:


#create 5*5 array for random no between 0 & 1
arr=np.random.rand(5,5)
print(arr)


# In[29]:


#Sum along the column
print(np.sum(arr,axis=0))


# In[30]:


#Sum along the row
print(np.sum(arr,axis=1))


# In[31]:


#calculate mean,median,sd and variance
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))


# In[32]:


#Sort an array
arr=np.random.rand(5,5)
print(arr)


# In[36]:


#Sort along the row
print(np.sort(arr,axis=1))


# In[42]:


#Append elements to array
arr=np.array([4,5,6,7])


# In[39]:


arr1=np.append(arr,8)
arr1


# In[40]:


arr2=np.append(arr,[9,10,11])
print(arr2)


# In[43]:


#Delete multiple elements
arr2=np.array([4,5,6,7,9,10,11])
print(arr2)
print('\n')
arr5=np.delete(arr2,[1,4])
print(arr5)


# In[44]:


#Combine and split an array
arr1=np.array([[1,2,3,4],[1,2,3,4]])
arr2=np.array([[5,6,7,8],[5,6,7,8]])


# In[47]:


#Combine the array items by column
cat=np.concatenate((arr1,arr2),axis=0)
print(cat)


# In[48]:


#Combine the array items by row
cat=np.concatenate((arr1,arr2),axis=1)
print(cat)


# In[ ]:




