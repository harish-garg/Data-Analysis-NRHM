#!/usr/bin/python

# Import the necessary modules
import os
import pandas as pd

# Dataset location
data_dir = 'DHIS (APRIL 15-MARCH 16)'

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
print "\n......\nWe are here..." + cwd + "\n......\n"

# get the paths for all the xls files in a list
file_list = []
for root, dirs, files in os.walk(data_dir, topdown=False):
    for name in files:
        file_list.append([os.path.join(root, name), root, name])
    
#print(file_list)
print('No of data files - ', str(len(file_list)))

# import the files into dataframes
dataframes = []

for f in file_list:
    print(f[0])
    dataframes.append(pd.read_excel(f[0]))
    
print(dataframes[0].head())
