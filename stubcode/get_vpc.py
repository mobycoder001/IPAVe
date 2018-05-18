#!/usr/bin/env python3 
import json
import boto3
import time
current_time=int(time.time())

ec2 = boto3.resource('ec2', region_name='us-west-2')
client = boto3.client('ec2')

#filters = [{'Name':'tag:Name', 'Values':['VPN*']}]

#vpcs = list(ec2.vpcs.filter(Filters=filters))
##import pdb; pdb.set_trace()
#vpcs = list(ec2.vpcs.filter(Filters=filters))

#for vpc in vpcs:
    #response = client.describe_vpcs(
        #VpcIds=[
            #vpc.id,
        #]
    #)
    #print(json.dumps(response, sort_keys=True, indent=4))

ec2 = boto3.resource("ec2")
for vpc in ec2.vpcs.all():
    for subnet in vpc.subnets.all():
        print(vpc, "all:", subnet)

    for az in ec2.meta.client.describe_availability_zones()["AvailabilityZones"]:
        for subnet in vpc.subnets.filter(Filters=[{"Name": "availabilityZone", "Values": [az["ZoneName"]]}]):
            print(vpc, az["ZoneName"], "filter:", subnet)

my_cidrs=[]
my_cidrs_csv=[]
for i in client.describe_subnets()['Subnets']:
    print(i['CidrBlock'])
    my_cidrs.append(i['CidrBlock'])


print('[*] my_cidrs: ')
for i in my_cidrs:
    print('[*] : ', i)

    x,y=i.split('/')
    #print(x, 'and', y, 'and', '1', 'and', current_time)
    #my_cidrs_csv.append("x, ',', y, ',', '1', ',', current_time")
    my_temp_string=x + ',' + y + ',' + '1' + ',' + str(current_time)
    print(my_temp_string)

    #my_cidrs_csv=[0,]

    

##import pdb; pdb.set_trace()
print('testing')
