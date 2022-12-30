#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


tips = sns.load_dataset('tips')


# In[4]:


tips.head()


# In[7]:


sns.displot(tips['total_bill'],kde=False,bins=40)


# In[8]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')


# In[9]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')


# In[10]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')


# In[11]:


sns.pairplot(tips,hue='sex',palette='coolwarm')


# In[12]:


sns.rugplot(tips['total_bill'])


# In[13]:


sns.displot(tips['total_bill'])


# In[ ]:




