#!/usr/bin/python
import os
rootdir = "./"

folder_list = []
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        new_filename = filename.split('_',2)[0] + "_" + filename.split('_',2)[1]
        folder_list.append(new_filename)
print(folder_list)