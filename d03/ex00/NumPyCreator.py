import numpy as np


class NumPyCreator:

    def from_list(lst, dtype = np.int64):
        return np.asarray(lst, dtype)

    def from_tuple(tpl, dtype = np.int64):
        return np.asarray(tpl, dtype)

    def from_iterable(itr, dtype = np.int64):
        return np.array(iter, dtype)

    def from_shape(shape, value = 0, dtype = np.int64):
        return np.full(shape, value, dtype)
    
    def random(shape):
        return np.random.random(shape)

    def identity(n, dtype = np.int64):
        return np.eye(n, dtype)

