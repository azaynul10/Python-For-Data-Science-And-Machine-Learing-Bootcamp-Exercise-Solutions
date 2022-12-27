#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


plt.show()


# In[5]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')


# In[9]:


fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,.5,.2,.2])

ax1.plot(x,y,color='red')
ax2.plot(x,y,color='red')


# In[12]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([.2,.2,.4,.4])

ax.plot(x,z)
ax.set_xlabel('X')
ax.set_ylabel('Z')

ax2.plot(x,y)
ax2.set_title('zoom')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])


# In[18]:


fig,axes = plt.subplots(1,2,figsize=(12,2))
axes[0].plot(x,y,color='blue',lw=3,ls='-')
axes[1].plot(x,y,color='red',lw=3,ls='--')


# In[ ]:




