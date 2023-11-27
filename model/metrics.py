import numpy as np
from lin_regression import LinearRegression 

def calculate_mse(y_actual, y_predicted):
    return np.mean(np.square(np.subtract(y_actual, y_predicted)))

def calculate_mae(y_true, predictions):
    return np.mean(np.abs(np.subtract(y_true, predictions)))

def calculate_r2_score(y_train, y_predicted):
    y_train_bar = np.mean(y_train)
    
    sum_squared_residual = np.sum(np.square(np.subtract(y_train, y_predicted)))
    sum_squared_total = np.sum(np.square(np.subtract(y_train, y_train_bar)))
    
    return 1 - (sum_squared_residual / sum_squared_total)

def fit_linear_regression(X_train, y_train, epochs, learn_rate):
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train, epochs, learn_rate)
    return lr_model

def predict_and_evaluate(model, X_test, y_test):
    test_predictions = model.predict(X_test)
    
    mse_test = calculate_mse(y_test, test_predictions)
    mae_test = calculate_mae(y_test, test_predictions)
    r2_test = calculate_r2_score(y_test, test_predictions)
    
    print("Test MSE:", mse_test)
    print("Test MAE:", mae_test)
    print("Test R2 Score:", r2_test)
