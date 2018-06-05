#!/usr/bin/env python3


# coding: utf-8
# ### Import modules#

import csv
import datetime
import ipaddress
import logging
import os
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


class render_graphs():
    #### Globals
    images_directory="./startflask/static/images/"
    total_addresses = 65534

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # create a file handler
    handler = logging.FileHandler('data_render.log')
    handler.setLevel(logging.INFO)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)
    logger.info('Starting graph rendering.')


    def read_data_gen_graphs(self):
        # ### Read in the csv and add headers to the columns
        df = pd.read_csv('../data/new_data.csv',
                         names = ['IP_Address', 'Subnet_mask', 'In_use?', 'unix_timestamp'])


        # ### Combine IP_Address and Subnet_mask columns to create IP_Network column
        df['IP_Network'] = df['IP_Address'] + '/' + df['Subnet_mask'].map(str)
        df


        # ### Convert IP_Address column to ipaddress.ip_address object and IP_Network column to ipaddress.ip_network object
        df['IP_Address'] = df['IP_Address'].apply(ipaddress.ip_address)
        df['IP_Network'] = df['IP_Network'].apply(ipaddress.ip_network)


        df


        # ### Create dictionary for ratio of 24 to 22 subnet masks
        dic = {22:4, 24:1}


        # # Add new column to hold ratio values
        df['mask_conversion'] = df['Subnet_mask'].map(dic)


        # ### Display new dataframe to verify new column addition
        df



        # ### Create new column for number of addresses per subnet
        df['num_addresses'] = (df['mask_conversion']*256)
        df

        # ### Output current dataframe
        self.logger.info(df)

        # ### Summing num_addresses column to get count of total IP addresses
        IP_count = df['num_addresses'].sum()
        count_24s = df['mask_conversion'].sum()
        self.logger.info("number of /24s:" + str(count_24s))


        # ### total addresses = number of addresses in a /16 network
        # ### Caluculated percent of a /16 network
        total_24s_per_16 = 256
        pct_16_used = (count_24s/total_24s_per_16)*100
        self.logger.info("percent used: {}".format(pct_16_used))

        # ### Pie chart of /24 usage per /16 network
        labels = 'IPs added', 'unused network'
        fracs = [IP_count, (self.total_addresses - IP_count)]
        explode = (0.05, 0)
        grid = GridSpec(1,1)
        plt.subplot(grid[0,0], aspect=1)
        plt.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
        plt.title("Percentage of /16 network utilized")
        plt.savefig("./startflask/static/images/IP_pct_pie", dpi=100)
        self.logger.info("wrote file IP_pct_pie")



        # ### Convert unix_timestamp to datetime and display new dataframe
        df['date'] = pd.to_datetime(df['unix_timestamp'], unit='s')
        df


        # ### Creating new dataframe for analyzing ip address additions over time
        ip_per_10sec = df[['date', 'mask_conversion']]


        # ### Setting index to date
        ip_per_10sec = ip_per_10sec.set_index(['date'])
        ip_per_10sec


        # ### Grouping by Date and summing the number of addresses per date group
        ip_per_10sec = ip_per_10sec.groupby(['date']).sum()


        # ### Number of IP addresses created every 10 seconds
        ip_per_10sec


        # ### Plot of number of IP addresses added to network at each point in time
        ###get_ipython().run_line_magic('matplotlib', 'inline')
        ip_per_10sec.plot()
        plt.ylabel("Number or IP Addresses")
        plt.xlabel("time")
        plt.title("IP Addresses added to network over time")
        plt.savefig("./startflask/static/images/IP_Addition", dpi=100)
        self.logger.info("wrote file IP_Addition")



        # ### Adding column to hold cumulative summation of  IP addresses over time
        ip_per_10sec['ip_cumul'] = ip_per_10sec['mask_conversion'].cumsum()
        ip_per_10sec


        # ### Unnecessarily creating new dataframe to plot accumulation of ip addresses on network over time
        ip = ip_per_10sec.reset_index()
        ips_over_time = ip[['date', 'ip_cumul']]


        ips_over_time = ips_over_time.set_index(['date'])
        ips_over_time


        # ### Plot of accumulation of IP adddresses on network over time
        ips_over_time.plot()
        plt.ylabel("Number or IP Addresses")
        plt.xlabel("time")
        plt.title("Accumulation of IP Addresses on network over time")
        plt.savefig( os.path.join(self.images_directory, "IP_Accumulation"), dpi=100)
        self.logger.info("wrote file IP_Accumulation")


if __name__ == '__main__':
    render=render_graphs()
    render.read_data_gen_graphs()
