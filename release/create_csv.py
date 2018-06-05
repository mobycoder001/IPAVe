#!/usr/bin/env python3


import get_cidrs_simple
import data_render




class csv_dump():


    csv_list = []


    def my_data_list(self, data_list):
        pass


    def create_csv(self, data_list):
        count=0
        while count < len(data_list):
            csvline=str(data_list[count]['ip_addr'])
            csvline= csvline + ',' + str(data_list[count]['cidr_mask'])
            csvline= csvline + ',' + str(data_list[count]['in_use'])
            csvline= csvline + ',' + str(data_list[count]['unixtime'])
            csvline= csvline + '\n'

            self.csv_list.append(csvline)

            count += 1;

        return self.csv_list


    def write_csv(self, csv_list, filename='../data/new_data.csv'):
        with open(filename, '+w') as fh:
            for i in self.csv_list:
                fh.write(i)


if __name__ == '__main__':
    agcs=get_cidrs_simple.awsGetCidrSimple()
    data_list=agcs.get_cidr_subnet()

    csvd=csv_dump()
    csvd.write_csv(csvd.create_csv(data_list))
