import numpy as np
import random

def train_test_split(X, y, test_size, random_state):
    if random_state is not None:
        random.seed(random_state)

    num_samples = X.shape[0]
    indices = list(range(num_samples))
    random.shuffle(indices)

    split_index = int(num_samples * (1 - test_size))
    train_indices = indices[:split_index]
    test_indices = indices[split_index:]

    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]

    return X_train, X_test, y_train, y_test
