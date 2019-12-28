#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#1D array
my_list= [1,2,3,4,5,6,7]


# In[3]:


my_list


# In[5]:


liar= np.array(my_list)


# In[6]:


liar


# In[7]:


#2D array(metrices)
mat = [[1,2,3],[4,5,6],[7,8,9]]


# In[8]:


armat = np.array(mat)


# In[9]:


armat


# In[18]:


#arange to generate a list(start,stop(exclusive),step count)
newmat=np.arange(0,21,2)


# newmat

# In[14]:


newmat


# In[16]:


np.zeros(3)


# In[17]:


#zeros using tuples((row,column)) for 2d arrays
np.zeros((3,3))


# In[20]:


#ones for 1D array
np.ones(4)


# In[22]:


#ones for 2D array using tuples((row,col))
np.ones((2,2))


# In[25]:


#using linspace for evenly spaced numbers from one point to another in a 1D array(start,stop,spacingor total numbers between start and stop)
np.linspace(0,5,10)


# In[27]:


#indentity matrix(row = col therefore only one no. is used here)
np.eye(4)


# In[28]:


#for random numbers between 0 to 1 
#1D
np.random.rand(5)


# In[31]:


#2D (rol,col)//no tuples here just the parameter for no. of rows and columns
np.random.rand(5,5)


# In[34]:


#for random distribution of numbers arround zero may be positive or negative
#1D
np.random.randn(5)


# In[35]:


#2D
np.random.randn(4,4)


# In[38]:


#random number between any two numbers(start(inclusive),stop(exclusive),total number of random numbers)
np.random.randint(1,100)#it will return a single random number


# In[39]:


np.random.randint(1,100,10)#it will return 10 random integers


# In[40]:


a1 = np.arange(1,26)


# In[41]:


a1


# In[56]:


#to change the dimension of original array(row,col)
a12= a1.reshape(5,5)


# In[44]:


#max value in an array
a2 = np.random.randint(1,100,10)


# In[45]:


a2


# In[46]:


a2.max()


# In[48]:


#minimum
a2.min()


# In[49]:


#index of maximum or minimum value in an array
a2.argmax()


# In[50]:


#min
a2.argmin()


# In[57]:


a12.max()


# In[58]:


a12.argmax()


# In[60]:


#shape of 1 or 2D array
a12.shape


# In[ ]:





# In[55]:


a1


# In[61]:


#datatype in the array
a1.dtype


# In[ ]:




