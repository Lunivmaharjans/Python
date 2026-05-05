import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def gradient_descent1(w_now, b_now, points1, learning_rate):
    w_gradient1 = 0
    b_gradient1 = 0

    n = len(points1)
    
    for i in range(n):
        x = points1.iloc[i].Temperature 
        y = points1.iloc[i].Revenue 

        w_gradient1 += (-2/n) * x *(y-(w_now * x + b_now))
        b_gradient1 += (-2/n) * (y-(w_now *x + b_now))
    w1 = w_now - learning_rate * w_gradient1
    b1 = b_now -learning_rate * b_gradient1

    return w1,b1
    
class LinearRegrassionModel:
    def _init_(self, learning_rate = 0.001, epochs = 1000, history_interval = 100):
        # self.weight = 0
        # self.bias = 0
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.history_interval = history_interval


    def mse(self, points1, w1, b1,x_col = None ,y_col = None):
        total_error = 0
        if x_col is None and y_col is None:
            columns =points1.columns.to_list()
            x_col = columns[0]
            y_col = columns[1]
        for i in range(len(points1)):
            x = points1.iloc[i].x
            y = points1.iloc[i].y
            total_error += (y - (w1*x + b1)) **2
        return total_error / len(points1)
    
    

model = LinearRegrassionModel()
points1 = pd.read_csv("IceCreamData.csv")

w1 = 0
b1 = 0
error = model.msc(points1,w1,b1,x_col="Temperature", y_col = "Revenue")
print(error)