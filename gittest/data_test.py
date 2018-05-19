#! /usr/bin/env python3

# coding: utf-8

# # Import modules# 

# In[13]:


import csv
import pandas as pd
import datetime


# # Read in the csv and add headers to the columns

# In[3]:


#df = pd.read_csv('c:/users/rusty/documents/moby/ipave/data/new_data.csv',
df = pd.read_csv('../data/new_data.csv',
                 names = ['IP_Address', 'Subnet_mask', 'In_use?', 'unix_timestamp'])


# # Print the dataframe

# In[4]:


df


# # Create dictionary for ratio of 24 to 22 subnet masks

# In[5]:


dic = {22:4, 24:1}


# # Add new column to hold ratio values

# In[6]:


df['mask_conversion'] = df['Subnet_mask'].map(dic)


# # Print new dataframe to verify new column addition

# In[7]:


df


# # Create new column for number of addresses per subnet

# In[9]:


df['num_addresses'] = (df['mask_conversion']*256)
df


# # Summing num_addresses column to get count of total IP addresses

# In[10]:


#IP_count = df['mask_conversion'].sum()
IP_count = df['num_addresses'].sum()
print("Number of IP Addresses:", IP_count)


# # total addresses = number of addresses in a /16 network 

# ### Caluculated percent of a /16 network

# In[14]:


total_addresses = 65534
pct_used = (IP_count/total_addresses)*100
print("percent used:", pct_used)


# Convert unix_timestamp to datetime and display new dataframe

# In[17]:


df['date'] = pd.to_datetime(df['unix_timestamp'], unit='s')
df


# In[12]:


#df2 = df[['unix_timestamp', 'IP_Address', 'Subnet_mask', 'In_use?']]a
df2 = df[['unix_timestamp', 'IP_Address', 'Subnet_mask', 'In_use?']]
df2


# In[31]:


df3 = df2.set_index(['unix_timestamp'])
df3


# In[32]:


#df3.set_value('1525670192', 'In_use?', 1)
df3.at['1525670192', 'In_use?'] =1
df3


# In[33]:


#df3 = df3.groupby(['unix_timestamp', 'IP_Address', 'In_use?']).agg(['count'])


# In[34]:


df4 = df3.reset_index()
df4.set_index(['unix_timestamp', 'IP_Address', 'In_use?']).unstack(level=-1)

def return_output(IP_count=IP_count,pct_used=pct_used):
	return(IP_count,pct_used)

for i in return_output():
    print(i)


