#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


np.zeros((10))


# In[5]:


np.ones((10))


# In[9]:


np.ones((10))*5


# In[15]:


np.arange(10,51)


# In[16]:


np.arange(10,51,2)


# In[17]:


np.arange(0,9).reshape(3,3)


# In[18]:


np.eye(3,3)


# In[24]:


np.random.rand(1)


# In[26]:


np.random.randn(25)


# In[28]:


np.arange(1,101).reshape(10,10)/100


# In[29]:


np.linspace(0,1,20)


# In[34]:


mat=np.arange(1,26).reshape(5,5)
mat


# In[40]:


mat[2:,1:]


# In[42]:


mat


# In[44]:


mat[3,4]


# In[45]:


mat[:3,1:2]


# In[46]:


mat[4,:]


# In[47]:


mat[3:5,]


# In[48]:


mat.sum()


# In[49]:


mat.std()


# In[51]:


mat.sum(axis=0)


# In[ ]:




