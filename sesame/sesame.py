# This file will contain the final program,
# for now it will be used for testing.

import numpy as np
np.seterr(divide = 'ignore') 
import matplotlib.pyplot as plt
from tools import fetch
from tools import tools

SHOW_PLOTS = False

# fetch.FetchAudioFromYoutube('https://www.youtube.com/watch?v=k1-TrAvp_xs', filename='mozart-lacrimosa')

data, sr = fetch.GetWav('mozart-lacrimosa.wav')
data = data.T[0]    # Remove stereo -> Getting the median is probably a better way (?)
print(f'{sr = }')
print(f'{data.shape = }')

# data = tools.PurgeData(data, 2)         # Do not purge when fingerprinting (!) -> loss of data results in wrong fingerprints
# print(f'After purge {data.shape = }')

sg = tools.GetSpectrogram(data, sr)

if SHOW_PLOTS:
    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(4)
    plt.subplot(2, 1, 1)
    plt.plot(data)  # This needs to be shifted to the right
    plt.subplot(2, 1, 2)
    plt.imshow(sg)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.show()

peaks = tools.GetPeaks(sg, 1.5) # At least 50% greater than surrounding elements
print(f'Number of peaks = {len(peaks)}')

peaks_y, peaks_x = peaks.T

print(peaks)

if SHOW_PLOTS:
    f = plt.figure()
    f.set_figwidth(10)
    f.set_figheight(4)
    plt.plot(peaks_x, peaks_y, 'o', color='black')
    plt.show()
    
fingerprints = tools.GenerateFingerprints(peaks)