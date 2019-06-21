import numpy as np
import pandas as p
#dropping rows having NA values
new_file = ['./new_file/file_beijing.csv','./new_file/file_shenyang.csv',
'./new_file/file_guangzhou.csv','./new_file/file_shanghai.csv','./new_file/file_chengdu.csv']
for cities in new_file:
    new_f = p.read_csv(cities)
    #droping all rows having NA cells
    new_f = new_f.dropna(axis = 0, subset=['TEMP','season','Iws','PRES','DEWP',
    'HUMI', 'cbwd', 'month', 'day', 'hour', 'PM_US Post'])
    index_null = new_f[new_f['PM_US Post']==0].index
    new_f.drop(index_null, inplace=True)
    new_f.to_csv(cities, index=False)
    #store the result in separate files



    