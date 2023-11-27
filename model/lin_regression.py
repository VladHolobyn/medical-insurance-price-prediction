import numpy as np

class LinearRegression():

    def __init__(self):
        pass

    def fit(self, X, y, epochs, learn_rate):
        rows, cols = X.shape
        self.weights = np.zeros(cols)
        self.b = 0

        for _ in range(epochs):
            y_pred = np.dot(X, self.weights) + self.b

            dw = (1/rows) * np.dot(X.T, (y_pred - y))
            db = (1/rows) * np.sum(y_pred - y)
            
            self.weights =  self.weights - learn_rate * dw
            self.b = self.b - learn_rate * db

    def predict(self, X):
        y = np.dot(X, self.weights) + self.b
        return y
