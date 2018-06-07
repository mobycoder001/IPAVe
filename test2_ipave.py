#!/usr/local/bin/python3

import unittest
import sys
import csv
#from IPAVe from IPAVe_program

# This class has some unittests that can be used to test IPAVe_program
class IPAVe (unittest.TestCase):
        #test to make sure that an string is input
    def string (self):
        self.string = string()
         #test the ipv6 is input correctly
    def ipv6(self):
         self.ipv6 = ipv6()
         str.assertEqual('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
         #test the ipv4 is input correctly
    def ipv4(self):
         self.ipv4 = ipv4()
         str.assertEqual('192.168.56.1')

class ReadData(unittest.TestCase):
    #checksfor the csv file
    def Parse_file_cvs(self):
        self.data= 'data.csv'

    def test_csv_read_data_headers(self):
        self.assertEqual(
            read_data(self.data)[0,1,2,3],
            ['IP_Address', 'Subnet_Mask', 'CIDR', ' TimeStamp',]
            )
    def test_IP_Address(self):
        self.assertEqual(read_data(self.data)[1][0], 'IP_Address')

    def test_Subnet_Mask(self):
        self.assertEqual(read_data(self.data)[3], '/24')

if __name__ == '__main__':
    unittest.main()


    
