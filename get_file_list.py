# Import modules
import os

data_dir = 'DHIS (APRIL 15-MARCH 16)'

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
print "We are here..." + cwd

# get the paths for all the xls files in a list
file_list = []

for root, dirs, files in os.walk(data_dir, topdown=False):
    for name in files:
        file_path = os.path.join(root, name)
        print(file_path)
        file_list.append(file_path)
    #for name in dirs:
        #print(os.path.join(root, name))

#print(file_list)
print(len(file_list))
