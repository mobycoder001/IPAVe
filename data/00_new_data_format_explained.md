

# Data formats

## CSV input

### Fields
IP_Address,Subnet_mask_in_CIDR_notation,0=False-1=True_is_this_IP_subnet_in_use,timestamp_in_unix_time

### Fields Descriptions
1. IP_Address - string nominal
1. Subnet_mask_in_CIDR_notation - integers nominal
1. 0=False-1=True_is_this_IP_subnet_in_use - boolean nominal
1. timestamp_in_unix_time - timestamp ordinal
1. datasource, a=aws,z=router
1. aws region
1. aws availability zone
1. aws subnet id
1. aws vpc id

### Available data AWS
1. IP Address
1. Subnet_mask_in_CIDR_notation
1. 0=False-1=True_is_this_IP_subnet_in_use
1. timestamp_in_unix_time (generated)

#### Available alt data in AWS
1. aws region
1. aws availability zone
1. aws subnet-id
1. aws vpc-id


### Available data Network Gear

1. IP Address
1. Subnet_mask_in_CIDR_notation
1. 0=False-1=True_is_this_IP_subnet_in_use
1. timestamp_in_unix_time (generated)


#### Available alt data in Network Gear
1. snmp location string parsing
1. 

## Database input
TBD

1. pass data to db modules as a list of list.
1. each line in the list is a field from the CSV


