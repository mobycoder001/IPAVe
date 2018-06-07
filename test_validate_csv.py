#!/usr/bin/env python3

""" A file which validates the .csv data format as described in the README.md doc for the data files."""
data_file_csv='../data/new_data.csv'

try:
    with open(data_file_csv,'r') as fh: 
        data=fh.readlines()
except Exception as e:
    print("[*] Error: ",e)

for i in data:
    print(i.strip().split(','));


for i in data:
    """example data string: 10.128.0.0,22,0,1525670182"""
    x0=i.strip().split(',')[0]    
    x1=i.strip().split(',')[1]    
    x2=i.strip().split(',')[2]    
    x3=i.strip().split(',')[3]    


    print("[*] begins var info testing")
    print(i.strip())
    x0=str(x0)
    x1=int(x1)
    x2=int(x2)
    x3=int(x3)

    print(type(x0))
    assert(str(x0))
    
    print(type(x1))
    assert(int(x1))

    print(type(x2))
    assert type(x2) is int, "value is not an integer: %r" % x2

    print(type(x3))
    assert(int(x3))

    print("[*] ends var info testing")

