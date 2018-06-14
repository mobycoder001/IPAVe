#!/usr/bin/env python3


# coding: utf-8
# ### Import modules#

#import csv
#import datetime
#import ipaddress
import logging
#import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


class render_graphs():
#    images_directory = "./startflask/static/images/"

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

    def read_data_format_df(self):
        # ### Read in the csv and add headers to the columns
        df = pd.read_csv('../data/new_data1.csv',
                         names=['IP_Address', 'Subnet_mask',
                                'In_use?', 'unix_timestamp'])
        dic = {22: 4, 24: 1, 20: 16}
        df['mask_conversion'] = df['Subnet_mask'].map(dic)
        df['date'] = pd.to_datetime(df['unix_timestamp'], unit='s')
        current_ips = df[['date', 'mask_conversion']]
        current_ips = current_ips.set_index(['date'])
        current_ips = current_ips.groupby(['date']).sum()
        return current_ips

    def plot_ips_over_time(self):
        current_ips = self.read_data_format_df()
        current_ips.plot(style='.-', rot=45, ax=None)
        plt.ylabel("number of IP addresses")
        plt.xlabel("time")
        plt.title("IP addresses added to network over time")
        plt.tight_layout()
        plt.savefig("./startflask/static/images/Current_IPs", dpi=100)
        self.logger.info("wrote file Current_IPs")

    def plot_pct_pie(self):
        current_ips = self.read_data_format_df()
        total_24s_per_16 = 256
        count_24s = current_ips['mask_conversion'][-1]
        labels = 'IPs in use', 'unused network'
        fracs = [count_24s, (total_24s_per_16 - count_24s)]
        explode = (0.05, 0)
        grid = GridSpec(1, 1)
        plt.subplot(grid[0, 0], aspect=1)
        plt.pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True)
        plt.savefig("./startflask/static/images/IP_pct_pie", dpi=100)
        self.logger.info("wrote file IP_pct_pie")


if __name__ == '__main__':
    render = render_graphs()
#    render.read_data_format_df()
    render.plot_ips_over_time()
    render.plot_pct_pie()
