#!/usr/bin/env python3


### notes on exporting the notebook images:
# https://stackoverflow.com/questions/32538758/nameerror-name-get-ipython-is-not-defined

# coding: utf-8

# # Import modules# 

# In[168]:


import csv
import pandas as pd
import datetime
import ipaddress


# # Read in the csv and add headers to the columns

# In[169]:


df = pd.read_csv('../data/new_data.csv',
                 names = ['IP_Address', 'Subnet_mask', 'In_use?', 'unix_timestamp'])


# # Combine IP_Address and Subnet_mask columns to create IP_Network column

# In[170]:


df['IP_Network'] = df['IP_Address'] + '/' + df['Subnet_mask'].map(str)
df


# # Convert IP_Address column to ipaddress.ip_address object and IP_Network column to ipaddress.ip_network object

# In[171]:


df['IP_Address'] = df['IP_Address'].apply(ipaddress.ip_address)
df['IP_Network'] = df['IP_Network'].apply(ipaddress.ip_network)


# In[172]:


df


# # Create dictionary for ratio of 24 to 22 subnet masks

# In[173]:


dic = {22:4, 24:1}


# # Add new column to hold ratio values

# In[174]:


df['mask_conversion'] = df['Subnet_mask'].map(dic)


# # Display new dataframe to verify new column addition

# In[175]:


df


# # Create new column for number of addresses per subnet

# In[176]:


df['num_addresses'] = (df['mask_conversion']*256)
df


# # Summing num_addresses column to get count of total IP addresses

# In[177]:


IP_count = df['num_addresses'].sum()
print("Number of IP Addresses:", IP_count)


# # total addresses = number of addresses in a /16 network
# ### Caluculated percent of a /16 network

# In[178]:


total_addresses = 65534
pct_used = (IP_count/total_addresses)*100
print("percent used:", pct_used)


# # Convert unix_timestamp to datetime and display new dataframe

# In[196]:


df['date'] = pd.to_datetime(df['unix_timestamp'], unit='s')
df


# In[197]:


ip_per_10sec = df[['date', 'num_addresses']]


# In[198]:


ip_per_10sec = ip_per_10sec.set_index(['date'])
ip_per_10sec
#df['minute'] = df['date'].apply()


# In[199]:


#ip_per_10sec.index = ip_per_10sec.index.map(lambda x: x.replace(second=0))
ip_per_10sec = ip_per_10sec.groupby(['date']).sum()


# In[200]:


ip_per_10sec


# In[201]:


#get_ipython().run_line_magic('matplotlib', 'inline')
ip_per_10sec.plot()


# In[203]:


#for i, row in ip_per_10sec.iterrows():
#  ifor_val = something
#  if <condition>:
#    ifor_val = something_else
#  df.set_value(i,'ifor',ifor_val)


#for i in ip_per_10sec.index:
#    if <something>:
#        df.at[i, 'ifor'] = x
#    else:
#        df.at[i, 'ifor'] = y

ip_per_10sec['ip_cum'] = ip_per_10sec['num_addresses'].cumsum()

ip_per_10sec


# In[205]:


ip = ip_per_10sec.reset_index()
ips_over_time = ip[['date', 'ip_cum']]


# In[207]:


ips_over_time = ips_over_time.set_index(['date'])

