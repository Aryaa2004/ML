#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


import os


# In[3]:


print(os.listdir("../input"))


# In[7]:


sales = pd.read_csv('supermarket_sales - Sheet1.csv')


# In[8]:


sales


# In[ ]:


sales['Date'] = pd.to_datetime(sales['Date'])


# In[ ]:


sales


# In[ ]:


sales['day'] = (sales['Date']).dt.day


# In[ ]:


sales


# In[ ]:


sales['month'] = (sales['Date']).dt.month


# In[4]:


sales['year'] = (sales['Date']).dt.year


# In[5]:


sales


# In[6]:


sales.describe()


# In[21]:


#Let's find the number of unique values in columns with object datatype


# In[22]:


categorical_cols = [cname for cname in sales.columns if sales[cname].dtype == 'object']


# In[23]:


categorical_cols


# In[24]:


sns.set(style = 'darkgrid')
gender_count = sns.countplot(x = 'Gender', data = sales).set_title('gender.count')


# In[25]:


sns.boxplot(x = 'Branch', y = 'gross income', data = sales).set_title('gross income according to branch')


# In[27]:


sns.boxplot(x = 'Branch', y = 'Rating',  data = sales).set_title('ratings by branch')


# In[28]:


sales['Time'] = pd.to_datetime(sales['Time'])


# In[29]:


sales


# In[30]:


sales['Hour'] = sales['Time'].dt.hour


# In[31]:


sales


# In[32]:


sales['Hour'].nunique()


# In[33]:


genderCount = sns.lineplot(x = 'Hour', y = 'Quantity', data = sales).set_title('Product sales per hour')


# In[35]:


sales['Rating'].unique()


# In[36]:


age_spend = sns.lineplot(x = 'Total', y = 'Rating', data = sales)


# In[37]:


sns.boxenplot(y = 'Product line', x = 'Quantity', data = sales)


# In[38]:


sns.countplot(y = 'Product line', data = sales, order = sales['Product line'].value_counts().index)


# In[ ]:




