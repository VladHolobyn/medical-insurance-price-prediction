import numpy as np
import random

def test_split(X, y, test_size, random_state):
    if random_state is not None:
        random.seed(random_state)

    num_samples = X.shape[0]
    indices = list(range(num_samples))
    random.shuffle(indices)

    split_index = int(num_samples * (1 - test_size))
    train_indices = indices[:split_index]
    test_indices = indices[split_index:]

    Xtrain, Xtest = X[train_indices], X[test_indices]
    ytrain, ytest = y[train_indices], y[test_indices]

    return Xtrain, Xtest, ytrain, ytest
