import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile,join
import os
#for loading and visualizing audio files
import librosa
import librosa.display
import librosa
import librosa.display
import numpy as np
#to play audio
#import IPython.display as ipd
path="C:\\Users\\SIDDHARTHA\\Downloads\\captcha88\\data\\8char-audio-cloud-v2-80k"
dest = "C:\\Users\\SIDDHARTHA\\Downloads\\captcha88\\data\\8char-audio-cloud-v2-80k\\specto"
files = [f for f in listdir(path) if isfile(join(path,f))]
#gray= file.open(self.directory_name + "/" + random_image_file)
#audio_clips = os.listdir(audio_fpath)
for audio in files:
    x, sr = librosa.load(os.path.join(path, audio))
    plt.figure(figsize=(1.28, .64), dpi=100)
    plt.axis('off')
    plt.axes([0., 0., 1., 1., ], frameon=False, xticks=[], yticks=[])
    S = librosa.feature.melspectrogram(y=x, sr=sr)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    plt.savefig(os.path.join(dest, os.path.splitext(audio)[0]+'.png'), bbox_inches=None, pad_inches=0)
    plt.close()