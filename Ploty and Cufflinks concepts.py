#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from plotly import __version__


# In[3]:


import cufflinks as cf


# In[4]:


from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[5]:


init_notebook_mode(connected=True)


# In[6]:


cf.go_offline()


# In[8]:


#DATA
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())


# In[9]:


df.head()


# In[10]:


df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})


# In[11]:


df2


# In[13]:


df.iplot()


# In[16]:


df.iplot(kind='scatter',x='A',y='B',mode='markers')


# In[17]:


df2.iplot(kind='bar',x='Category',y='Values')


# In[18]:


df.sum().iplot(kind='bar')


# In[19]:


df.iplot(kind='box')


# In[21]:


df3=pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,40,50],'z':[5,4,3,2,1]})


# In[23]:


df3.iplot(kind='surface',colorscale='rdylbu')


# In[25]:


df['A'].iplot(kind='hist',bins=50)


# In[27]:


df[['A','B']].iplot(kind='spread')


# In[28]:


df.iplot(kind='bubble',x='A',y='B',size='C')


# In[29]:


df.scatter_matrix()


# In[ ]:




