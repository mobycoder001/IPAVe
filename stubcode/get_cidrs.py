#!/usr/bin/env python3


import json
import boto3
import time
current_time=int(time.time())

ec2 = boto3.resource('ec2', region_name='us-west-2')
client = boto3.client('ec2')


def get_regions():
    """either configure active regions here or derive regions from aws"""
    """future code
    returns: l_regions : list of region names
    """
    pass

def enumerate_vpc_subnets():
    """WIP"""
    for vpc in ec2.vpcs.all():
        for subnet in vpc.subnets.all():
            print(vpc, "all:", subnet)

        for az in ec2.meta.client.describe_availability_zones()["AvailabilityZones"]:
            for subnet in vpc.subnets.filter(Filters=[{"Name": "availabilityZone", "Values": [az["ZoneName"]]}]):
                print(vpc, az["ZoneName"], "filter:", subnet)



def get_subnets_only():
    """Collect subnets from VPC / region"""
    my_cidrs=[]
    my_cidrs_csv=[]
    #print('[*] my_cidrs: ')

    for i in client.describe_subnets()['Subnets']:
        #print(i['CidrBlock'])
        my_cidrs.append(i['CidrBlock'])


    for i in my_cidrs:
        #print('[*] : ', i)

        x,y=i.split('/')

        my_temp_string = x + ',' + y + ',' + '1' + ',' + str(current_time)
        my_cidrs_csv.append(my_temp_string)
        #print(my_temp_string)

    return(my_cidrs_csv)

        #my_cidrs_csv=[0,]

# Add formatting for data discovery output.  Select specific IDs useful for database population.
for i in client.describe_subnets()['Subnets']:
    print('[*] SubnetID: {} CidrBlock: {}'.format(i['SubnetId'],i['CidrBlock']))



if __name__ == '__main__':
    enumerate_vpc_subnets()
    get_subnets_only()

    print('[*] function checking: ')
    for i in get_subnets_only():
        print(i)
