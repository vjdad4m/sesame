import numpy as np

def PurgeData(data, level):
    for i in range(level):
        data = np.delete(data, np.arange(0, data.size, 2))
    return data