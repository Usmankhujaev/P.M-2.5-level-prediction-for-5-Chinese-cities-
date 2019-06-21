# P.M-2.5-level-prediction-for-5-Chinese-cities-
This is a system implementation that can predict the PM 2.5  level using previous data of five Chinese cities dataset
How to handle with datasets? Beijing file had 4 PM values while other cities had only 3 incoming PM values 
In order to make balance in dataset, I manually add one column and make every column name be the same in each file, 
you can see preprocessing file in the the same named folder

If you run csv_reader.py file, that file wil create you five new files with filling the NA spaces of PM_US_Post column
This is the algorithm to calculate missing PM_US Post values at missing places from other PM stations. For example in case of missing values,
if two columns are missing then just copy the value of the existing station, if 1 is missing then take the average of 3 and so on.
EX:
NA = 𝑖𝑛𝑡((123+138)/2) =130 
NA = 𝑖𝑛𝑡((79+70+75)/3) = 74

In dataset you have two types of data
1) Numerical data - most of the data in columns were having format of int or float such as (year, month, day, PM_US_Post, HUMI, PRES etc)
2) Categorical data - these types of data were converted to int format for example (cbwd converted into binary 0 or 1 values)

The new created file was having this format because I have dropped other PM columns, first column and last two columns since 
there were containing meaningless information. Then use null_remove.py code to drop all NA containing rows.


![Alt text](/Figure_1.png)
