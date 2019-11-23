"""
Converts given mp3 files to wav format
"""

import pydub as pd
from progressbar import ProgressBar
import os

pd.AudioSegment.converter = "C:\\Users\\SIDDHARTHA\\Downloads\\ffmpeg-4.2.1-win64-static\\bin\\ffmpeg.exe"
pd.AudioSegment.ffmpeg = "C:\\Users\\SIDDHARTHA\\Downloads\\ffmpeg-4.2.1-win64-static\\bin\\ffmpeg.exe"
pd.AudioSegment.ffprobe = "C:\\Users\\SIDDHARTHA\\Downloads\\ffmpeg-4.2.1-win64-static\\bin\\ffprobe.exe"

#change absolute path to source directory
src="C:\\Users\\SIDDHARTHA\\Downloads\\19301936-project3\\training_audio"

pbar=ProgressBar()
for file in pbar(os.listdir(src)):
    dest=str(file).split('.')[0]+".wav"
    sound=pd.AudioSegment.from_mp3(src+"\\"+file)
    sound.export(dest,format="wav")