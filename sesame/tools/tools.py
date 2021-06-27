from re import X
import numpy as np
import librosa
import hashlib
from tqdm import trange

def PurgeData(data, level):
    for i in range(level):
        data = np.delete(data, np.arange(0, data.size, 2))
    return data

# Spectrogram from https://stackoverflow.com/questions/56719138/how-can-i-save-a-librosa-spectrogram-plot-as-a-specific-sized-image/57204349#57204349
def scale_minmax(X, min=0.0, max=1.0):
    X_std = (X - X.min()) / (X.max() - X.min())
    X_scaled = X_std * (max - min) + min
    return X_scaled

def spectrogram_image(y, sr, out, hop_length, n_mels):
    mels = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels,n_fft=hop_length*2, hop_length=hop_length)
    mels = np.log(mels + 1e-9)
    img = scale_minmax(mels, 0, 255).astype(np.uint8)
    img = np.flip(img, axis=0)
    return img

def GetSpectrogram(data, sr):
    hop_length = 512
    n_mels = 128
    out = 'out.png'
    sg = spectrogram_image(data, sr=sr, out=out, hop_length=hop_length, n_mels=n_mels)
    return sg

def HashSha256(s):
    return hashlib.sha256(s.encode()).hexdigest() # Might change to a faster hashing algorithm later

def GetPeaks(sg, r):
    print('Getting peaks...')
    h, w = sg.shape
    peaks = []
    for y in trange(1,h-1):
        for x in trange(1,w-1, leave=False):
            if sg[y][x] > sg[y-1][x] * r and sg[y][x] > sg[y][x-1] * r and sg[y][x] > sg[y+1][x] * r and sg[y][x] > sg[y][x+1] * r:
                peaks.append((y, x))
    return np.array(peaks)