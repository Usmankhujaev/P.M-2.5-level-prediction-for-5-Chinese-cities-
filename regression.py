import pandas as p
import numpy as np
import matplotlib.pyplot as matplot
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

from math import sqrt

final_csv = './dataset.csv' 
new_file = [
'./new_file/file_beijing.csv',
'./new_file/file_shenyang.csv',
'./new_file/file_guangzhou.csv',
'./new_file/file_shanghai.csv',
'./new_file/file_chengdu.csv' ]
list_of_cities = []
for cities in new_file:
    data = p.read_csv(cities)
    list_of_cities.append(data)
data = p.concat(list_of_cities, sort=False)
#remove negative values and outliers from dataset (outliers)
for outliers, rows in data.iterrows():
    if (rows['HUMI'] < 0):
        data.drop(outliers, inplace=True)
    if (rows["PM_US Post"] > 900):
        data.drop(outliers, inplace=True)
data = p.concat([data, p.get_dummies(data['cbwd'], prefix='dir')], axis=1)
data.drop(['cbwd'], inplace=True, axis=1)
season = data.pop('season')
data['spring'] = (season==1) *  1
data['summer'] = (season==2) *  1
data['fall'] = (season==3) *  1
data['winter'] = (season==4) *  1

data.to_csv(final_csv)
# split our target column 'PM_US Post'
y = data['PM_US Post']
x_drop = data.drop(['PM_US Post'],axis =1)

#Starting train part
x_train, x_test, y_train, y_test = train_test_split(x_drop,
y, test_size=0.15, random_state=1234)

linerar_regression = LinearRegression()
linerar_regression.fit(x_train, y_train)

random_forest = RandomForestRegressor(n_estimators=200,
random_state=2000)
random_forest.fit(x_train, y_train)

#prediction x_test and y_test
linear_prediction = linerar_regression.predict(x_test)
linerar_regression_pred=linerar_regression.score(x_test, y_test)
print("Linear regression prediction: " , linerar_regression_pred)
mse_lr = sqrt(mean_squared_error(y_test, linear_prediction,))
r2_lr = r2_score(y_test, linear_prediction)
print("Mean squared error: ", mse_lr)
print("R2 score: ", r2_lr)
#random forest predictions
random_prediction = random_forest.predict(x_test)
random_forest_pred = random_forest.score(x_test, y_test)
print("Random Forest prediction: " , random_forest_pred)
print("Mean squared error: %.3f" % 
sqrt(mean_squared_error(y_test, random_prediction))) 
print("R2 score: %.3f" % r2_score(y_test, random_prediction))

matplot.title('Predicted vs Actual using Random Forest')
matplot.scatter(y_test, random_prediction)
matplot.xlabel("Actual values")
matplot.ylabel("Predicted values")
matplot.show()


#uncomment the code below to see the plot function and the result of it
'''
matplot.close('all')
a = data['HUMI']
b = data['TEMP']
c = data['PRES']
d = data['Iws']
f = data['PM_US Post']
matplot.figure(figsize=(16,9))
matplot.subplot(131)
matplot.scatter(a,f)
matplot.subplot(132)
matplot.scatter(b,f)
matplot.subplot(133)
matplot.scatter(d,f)
#matplot.subplot(221)
matplot.suptitle('PM_US Post values')

matplot.show()

'''
