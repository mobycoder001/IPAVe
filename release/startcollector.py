#!/usr/bin/env python3

import get_cidrs_simple
import data_render
import create_csv

if __name__ == '__main__':
    # Collect the data
    agcs=get_cidrs_simple.awsGetCidrSimple()
    data_list=agcs.get_cidr_subnet()


    csvd=create_csv.csv_dump()
    csvd.write_csv(csvd.create_csv(data_list))

    #populate_database(data_list)
    #create_csv(data_list)

    # Render the graphs
    render=data_render.render_graphs()
    render.read_data_gen_graphs()
