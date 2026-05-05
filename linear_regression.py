import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class linearregressionmodel:
    def _init_(self, learning_rate = 0.001, epochs = 1000, history_interval = 100):
        # self.weight = 0
        # self.bias = 0
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.history_interval = history_interval
        
    def gradient_descent(self, w_now, b_now, points, x_col = None, y_col = None):
        if x_col is None and y_col is None:
            columns = points.columns.to_list()
            x_col = columns[0]
            y_col = columns[1]
        
        w_gradient = 0
        b_gradient = 0
    
        n = len(points)
    
        for i in range(n):
            x = points.iloc[i][x_col]
            y = points.iloc[i][y_col]
            residual = (y - (w_now * x + b_now))
        
        w_gradient += (-2/n) * x * residual
        b_gradient += (-2/n) * residual
        
        w = w_now - self.learning_rate * w_gradient
        b = b_now - self.learning_rate * b_gradient
        
    def mse(self, points, w, b, x_col = None, y_col = None):
        if x_col is None and y_col is None:
            columns = points.columns.to_list()
            x_col = columns[0]
            y_col = columns[1]
        
        total_error = 0
        for i in range(len(points)):
            x = points.iloc[i][x_col]
            y = points.iloc[i][y_col]
        total_error += (y - (w*x + b)) **2
        return total_error / len(points)
    
    

model = linearregressionmodel()
points = pd.read_csv("IceCreamData.csv")
        
w = 0
b = 0

error = model.mse(points, w, b)
# error = model.mse(points, w, b, x_col = "Temperature", y_col = "Revenue")

print(error)