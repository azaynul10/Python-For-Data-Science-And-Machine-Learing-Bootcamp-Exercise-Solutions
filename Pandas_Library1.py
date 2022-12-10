#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np


# In[75]:


import pandas as pd


# In[3]:


labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}


# In[6]:


pd.Series(arr,labels)


# In[7]:


ser1=pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
ser2=pd.Series([1,2,3,4],['USA','Germany','Italy',"Japan"])


# In[8]:


ser1+ser2


# In[11]:


from numpy.random import randn


# In[4]:


np.random.seed(101)


# In[7]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[8]:


df


# In[9]:


df['new'] = df['W'] + df['Y']


# In[10]:


df


# In[11]:


df.drop('new',axis=1,inplace=True)


# In[12]:


df


# In[13]:


df.loc[['A','B'],['W','Y']]


# In[14]:


df.loc['B','Y']


# In[15]:


df.iloc[2]


# In[18]:


df[df['W']>0][['Y','X']]


# In[20]:


boolser = df['W']>0
result = df[boolser]
mycols = ['Y','X']
result[mycols]


# In[5]:


outside = ['G1','G1','G1','G2','G2','G2']
inside =[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)


# In[13]:


df=pd.DataFrame(randn(6,2),hier_index,['A','B'])


# In[14]:


df


# In[17]:


df.index.names = ['Groups','Num']


# In[18]:


df


# In[19]:


df.xs(1,level='Num')


# In[20]:


d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}


# In[21]:


df=pd.DataFrame(d)


# In[22]:


df


# In[24]:


df.dropna(thresh=2)


# In[25]:


df.fillna(value='FILL IN VALUE')


# In[28]:


data = {'Company':['Google','Google','Microsoft','Microsoft','Facebook','Facebook'],
        'Person':['Sam','karl','Charlie','Michael','Vanessa','Zayn'],
        'Sales':[200,340,550,420,120,320]}


# In[29]:


df = pd.DataFrame(data)


# In[30]:


df.groupby('Company').describe()


# In[31]:


df.groupby('Company').describe().transpose()['Facebook']


# In[32]:


df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
                   columns=['letter', 'number', 'animal'])


# In[33]:


df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])


# In[34]:


pd.concat([df1, df3], join="inner")


# In[35]:


df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})


# In[36]:


other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'B': ['B0', 'B1', 'B2']})


# In[42]:


df.join(other, lsuffix='_caller', rsuffix='_other')


# In[45]:


df=pd.DataFrame({'col1':[1,2,3,4],
                'col2':[444,555,666,444],
                'col3':['abc','xyz','gif','nmn']})
df.head()


# In[47]:


df['col2'].nunique()


# In[49]:


df['col2'].value_counts()


# In[55]:


df[(df['col1']>2) &  (df['col2']==444)]


# In[54]:


def times2(x):
    return x*x
df['col1'].apply(times2)


# In[60]:


df['col1'].apply(lambda x:x*x)


# In[61]:


df['col3'].apply(len)


# In[62]:


df.columns


# In[63]:


df.index


# In[64]:


df.sort_values('col2')


# In[65]:


df.isnull()


# In[71]:


data = {'A':['foo','foo','foo','bar','bar','bar'],
       'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]
       }
df = pd.DataFrame(data)


# In[73]:


df.pivot_table(values='D',index=['A','B'],columns=['C'])


# In[77]:


df.to_csv('My_output',index=False)


# In[78]:


df.read_csv('My_output')


# In[79]:


pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')


# In[82]:


data=pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')


# In[85]:


data[0].head()


# In[87]:


from sqlalchemy import create_engine


# In[88]:


engine = create_engine('sqlite:///:memory:')


# In[92]:


sqldf = df.to_sql('my_table', con=engine)


# In[94]:


sqldf


# In[95]:


df.to_sql('my_table',engine)


# In[ ]:




