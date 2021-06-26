import numpy as np
from scipy import signal

def PurgeData(data, level):
    for i in range(level):
        data = np.delete(data, np.arange(0, data.size, 2))
    return data

def GetSpectrogram(data, sr):
    frequencies, times, spectrogram = signal.spectrogram(data, sr)
    return spectrogram, frequencies, times