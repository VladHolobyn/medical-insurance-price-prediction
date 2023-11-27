import numpy as np

def calculate_mse(y_actual, y_predicted):
    mse = np.mean((y_actual - y_predicted)**2)
    return mse

def calculate_mae(y_true, predictions):
    y_true, predictions = np.array(y_true), np.array(predictions)
    return np.mean(np.abs(y_true - predictions))

def calculate_r2_score(y_train, y_predicted):
    y_train_bar = np.mean(y_train)

    sum_squared_residual = ((y_train - y_predicted)**2).sum()
    sum_squared_total = ((y_train - y_train_bar)**2).sum()

    return 1 - (sum_squared_residual/sum_squared_total)