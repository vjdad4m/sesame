import os
import soundfile as sf

datadir = os.path.abspath(__file__)[:-9] + '/../../data/'

# Use for personal use only, you need to have youtuble-dl installed
def FetchAudioFromYoutube(link, filename='audio', format='wav'):
    os.system(f'youtube-dl --extract-audio --output "{datadir}{filename}.%(ext)s" --audio-format {format} {link}')

def GetWav(filename):
    data, sr = sf.read(datadir + filename)
    return data, sr