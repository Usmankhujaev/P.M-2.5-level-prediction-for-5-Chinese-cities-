import numpy as np
import pandas as p
import csv
#open all csv files one by one
files = ['./file_beijing.csv','./file_shenyang.csv','./file_guangzhou.csv',
'./file_shanghai.csv','./file_chengdu.csv']
#new csv file storage location
new_file = ['./new_file/file_beijing.csv','./new_file/file_shenyang.csv',
'./new_file/file_guangzhou.csv','./new_file/file_shanghai.csv','./new_file/file_chengdu.csv']
for cities in range(len(files)):
    f = open(new_file[cities], "w", newline='')
    csvwriter = csv.writer(f, delimiter=',')
    with open(files[cities], 'r') as myfile:
        column = csv.reader(myfile, delimiter=',')
        for col in list(myfile):
            column = col.split(",") 
            #take the NULL values of 'PM_US Post' and fill with the average of neighbor values  
            if (column[9] == 'NA'): 
                us_post = 0
                diviser = 3
                for line in range(6,9):
                    if(column[line] != 'NA'):
                        us_post += (int(column[line]))
                    if(column[line] == 'NA'):
                        diviser = diviser - 1 
                    if(diviser == 0):
                        diviser = 1
                        continue
                column[9] = str(int(us_post/diviser))
            csvwriter.writerow([column[1],column[2], column[3], column[4],column[5], column[9],
            column[10],column[11], column[12], column[13],column[14], column[15]])         




