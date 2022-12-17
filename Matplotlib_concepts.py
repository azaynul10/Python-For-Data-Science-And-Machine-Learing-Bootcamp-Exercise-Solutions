#!/usr/bin/env python
# coding: utf-8

# In[42]:


import matplotlib.pyplot as plt


# In[41]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import numpy as np
x = np.linspace(0,5,11)
y = x**2


# In[43]:


x


# In[44]:


y


# In[9]:


#FUNCTIONAL
plt.plot(x,y)
plt.show()


# In[45]:


plt.plot(x,y)
plt.xlabel('X  Label')
plt.ylabel('Y Label')
plt.title('Title')


# In[46]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[13]:


#OO
fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')


# In[17]:


fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.1,0.5,0.4,0.3])

axes1.plot(x,y)
axes1.set_title('LARGER PLOT')

axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')


# In[18]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y)


# In[20]:


fig,axes=plt.subplots(nrows=1,ncols=2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')

plt.tight_layout()


# In[25]:


fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(8,2))

axes[0].plot(x,y)

axes[1].plot(y,x)

plt.tight_layout()


# In[26]:


fig.savefig('my_picture.png',dpi=200)


# In[30]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,x**2,label='X Squared')
ax.plot(x,x**3,label='X Cubed')

ax.legend(loc=(0.1,0.1))


# In[40]:


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,color='purple',lw=3,alpha=0.5,ls='--',marker='o',markersize=20,markerfacecolor='yellow',markeredgewidth=3,markeredgecolor='green')

ax.set_xlim([0,1])
ax.set_ylim([0,2])


# In[ ]:




