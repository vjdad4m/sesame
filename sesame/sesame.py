# This file will contain the final program,
# for now it will be used for testing.

import numpy as np
import matplotlib.pyplot as plt
from tools import fetch
from tools import tools

# fetch.FetchAudioFromYoutube('https://www.youtube.com/watch?v=k1-TrAvp_xs', filename='mozart-lacrimosa')

data, sr = fetch.GetWav('mozart-lacrimosa.wav')
data = data.T[0]    # Remove stereo -> Getting the median is probably a better way (?)
print(f'{sr = }')
print(f'{data.shape = }')

data = tools.PurgeData(data, 5)         # Do not purge when fingerprinting (!) -> loss of data results in wrong fingerprints
print(f'After purge {data.shape = }')

plt.plot(data)
plt.show()