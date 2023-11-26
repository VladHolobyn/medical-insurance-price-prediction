import numpy as np

def split_data(x_data, y_data, ratio, seed):
    np.random.seed(seed)

    split_index = int(len(x_data) * ratio)

    shuffled_indices = np.random.permutation(len(x_data))

    x_train = x_data[shuffled_indices[:split_index]]
    x_test = x_data[shuffled_indices[split_index:]]
    y_train = y_data[shuffled_indices[:split_index]]
    y_test = y_data[shuffled_indices[split_index:]]

    return [x_train, x_test, y_train, y_test]