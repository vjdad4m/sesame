# This file will contain the final program,
# for now it will be used for testing.

import numpy as np
np.seterr(divide = 'ignore') 
import matplotlib.pyplot as plt
from tools import fetch
from tools import tools

# fetch.FetchAudioFromYoutube('https://www.youtube.com/watch?v=k1-TrAvp_xs', filename='mozart-lacrimosa')

data, sr = fetch.GetWav('mozart-lacrimosa.wav')
data = data.T[0]    # Remove stereo -> Getting the median is probably a better way (?)
print(f'{sr = }')
print(f'{data.shape = }')

data = tools.PurgeData(data, 2)         # Do not purge when fingerprinting (!) -> loss of data results in wrong fingerprints
print(f'After purge {data.shape = }')

f = plt.figure()
f.set_figwidth(10)
f.set_figheight(4)
plt.subplot(2, 1, 1)
plt.plot(data)  # This needs to be shifted to the right
plt.subplot(2, 1, 2)
# sg = plt.specgram(data, Fs = sr, cmap='jet')
sg = tools.GetSpectrogram(data, sr)
plt.imshow(sg)
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.show()