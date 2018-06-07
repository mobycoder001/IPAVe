#!/usr/bin/env python3
#Name: Manuel Duarte
#Program: Test for IPV4 and IPV6

import socket
def test_validateipv4ip(address): #this funtion tests for IPV4
    try:
        socket.inet_aton(address)
        print ("Correct IPv4 IP") 
    except socket.error:
        print ("wrong IPv4 IP") # If IPV4 is wrong
def test_validateipv6ip(address): #this function tests for IPV6
### for IPv6 IP address validation
    try:
        socket.inet_pton(socket.AF_INET6,address)
        print ("Correct IPv6 IP")
    except socket.error:
        print ("wrong IPv6 IP") # if IPV6 is wrong
#correct IPs:
test_validateipv4ip("192.168.3.1")
test_validateipv6ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
#Wrong IPs:
test_validateipv4ip("192.168.6.500")
test_validateipv6ip("2001:0db8:85a3:0000:0000:8b4t2e")
