#!/usr/bin/env python3

import json
import boto3
import time
import logging

current_time=int(time.time())

ec2 = boto3.resource('ec2', region_name='us-west-2')
client = boto3.client('ec2')

class awsGetCidrSimple():
    """Collect information about in use VPC information.
    # data format:
    # struct_csv = { 'ip_addr' : "10.0.0.0", 'cidr_mask' : '24', 'in_use' : 1, 'unixtime' : '234567', }
    # data_list = []  # array of struct_csv

    """

    data_list = []

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # create file handler
    handler = logging.FileHandler('aws_cidr_collect.log')
    handler.setLevel(logging.INFO)
    # create logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add handlers to the logger
    logger.addHandler(handler)
    logger.info('Starting aws collect log.')


    def get_cidr_subnet(self):
        """Collect information about VPC subnets in use.

        returns: data_list / JSON object including information about subnet pairs.

        """
        for i in client.describe_subnets()['Subnets']:
            self.logger.info('[*] [added] CidrBlock: {} from SubnetID: {} '.format(i['CidrBlock'],i['SubnetId']))

            self.data_list.append({ 'ip_addr' : i['CidrBlock'].split('/')[0], 'cidr_mask' : i['CidrBlock'].split('/')[1], 'in_use' : 1, 'unixtime' : '234567', })

        return self.data_list


if __name__ == '__main__':
    agcs=awsGetCidrSimple()
    data_list=agcs.get_cidr_subnet()
    print('[*] [ __main__ ] Data List: ')
    for i in data_list:
        print(i)
