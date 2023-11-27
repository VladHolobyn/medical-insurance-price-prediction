import numpy as np

def test_split(X, y, test_size, random_state):
    np.random.seed(random_state)

    split_index = int(len(X) * test_size)

    shuffled_indices = np.random.permutation(len(X))

    xtrain = X[shuffled_indices[:split_index]]
    xtest = X[shuffled_indices[split_index:]]
    ytrain = y[shuffled_indices[:split_index]]
    ytest = y[shuffled_indices[split_index:]]

    return [xtrain, xtest, ytrain, ytest]