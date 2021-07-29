#!/usr/bin/env python
# coding: utf-8

# In[1]:


# two workhorse data structures: Series and DataFrame.


# In[2]:


import pandas as pd
import numpy  as np


# In[3]:


# Series
# A Series is a one-dimensional array-like object containing a sequence 
# of values (of similar types to NumPy types) and an associated array of 
# data labels, called its index.


# In[4]:


list(['Jberg', 'east london', 'cape town'])


# In[5]:


series1 = pd.Series(data=list('abcd'))
series1


# In[6]:


c_1 = pd.Series(data=['Jberg', 'east london', 'cape town'])   
c_1.index


# In[7]:


obj = pd.Series([4, 7, -5, 3])
obj>4


# In[8]:


obj2 = pd.Series(index=['d', 'b', 'a', 'a'], data=[4, 7.0, -5, 3] )
obj2


# In[9]:


obj2.index[0:3]


# In[10]:


obj2=[1,3,5,6]


# In[11]:


obj1=[2,4,5,6,] 
n=(obj2)*(obj1)


# In[ ]:


obj2[['c', 'a', 'd']]


# In[ ]:


print(obj2)


# In[ ]:


# Using NumPy functions or NumPy-like operations


# In[ ]:


obj2 > 3


# In[ ]:


obj2[obj2 > 0]


# In[ ]:


obj2 * 2


# In[ ]:


np_cities = np.array(['Blore', 'delhi', 'chennai'])


# In[ ]:


series_cities = pd.Series(np_cities)
series_cities


# In[ ]:


# series is sort of dict
# as it is a mapping of index values to data values


# In[ ]:


obj2


# In[ ]:


'b' in obj2


# In[ ]:


'e' in obj2


# In[ ]:


# building Series from Python dict
# dict keys ==> index
# dict values ==> Series values
# Resultant Series is sorted
citydata = {'Hybd': 35000, 
            'Bangalore': 71000, 
            'Delhi': 16000, 
            'Chennai': 5000}


# In[ ]:


obj3 = pd.Series(citydata)
obj3


# In[ ]:


# override the dict key as index
citynames = ['Bangalore', 'Delhi', 'Hybd', 'Chennai']


# In[ ]:


obj4 = pd.Series(citydata, index=citynames)
obj4


# In[ ]:


# A useful Series feature for many applications is that it automatically 
# aligns by index label in arithmetic operations
# more like RDBMS join operation


# In[ ]:


obj3 + obj4


# In[ ]:


# series from scalar input

scalar_series = pd.Series(100, index=['pos1', 'pos2','pos3'])
scalar_series


# In[ ]:


scalar_series = pd.Series([100, 200, 300], index=['pos1', 'pos2','pos3'])
scalar_series


# In[ ]:


# access series
scalar_series[0]


# In[ ]:


# access series
scalar_series['pos1']


# In[ ]:


# access series
scalar_series['pos1': 'pos3']


# In[ ]:


# vectorize operations
vector1 = pd.Series([1,2,3,4], index=['a', 'b','c','d'])
vector2 = pd.Series([10,20,30,40], index=['a', 'b','c','d'])


# In[ ]:


vector1 + vector2


# In[ ]:


vector1 * vector2


# In[ ]:


vector1 / vector2


# In[ ]:


vector3 = pd.Series([10,20,300,400], index=['a', 'b','e','f'])


# In[ ]:


vector1 + vector3


# In[ ]:


city = pd.Series(list(['Jberg', 'east london', 'cape town'])
print (city)


# In[13]:


reliance_data1=pd.read_csv (r'C:\Users\Satnam\dataset\fist_file.csv')


# In[15]:


reliance_data1


# In[16]:


reliance_data1.head(10)


# In[17]:


reliance_data1.values


# In[19]:


reliance_data1.describe(include="all")


# In[ ]:




