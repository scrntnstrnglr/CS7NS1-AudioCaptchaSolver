"""
Converts wav files to spectrograms
"""
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile,join
import os
import librosa
import librosa.display
import librosa
import librosa.display
import numpy as np
import argparse
from progressbar import ProgressBar
import pydub as pd

pd.AudioSegment.converter = "C:\\Users\\SIDDHARTHA\\Downloads\\ffmpeg-4.2.1-win64-static\\bin\\ffmpeg.exe"
pd.AudioSegment.ffmpeg = "C:\\Users\\SIDDHARTHA\\Downloads\\ffmpeg-4.2.1-win64-static\\bin\\ffmpeg.exe"
pd.AudioSegment.ffprobe = "C:\\Users\\SIDDHARTHA\\Downloads\\ffmpeg-4.2.1-win64-static\\bin\\ffprobe.exe"

"""
def convertToWAV(path,target):
    pbar=ProgressBar()
    for file in pbar(os.listdir(path)):
        dest=str(file).split('.')[0]+".wav"
        sound=pd.AudioSegment.from_mp3(path+"\\"+file)
        sound.export(join(target,dest),format="wav")
    pbar.finish()
"""
    
def convertToSpectogram(path,dest,length,width):
    pbar=ProgressBar()
    #path="C:\\Users\\SIDDHARTHA\\Downloads\\19301936-project3\\AudioWAV"
    #dest = "C:\\Users\\SIDDHARTHA\\Downloads\\19301936-project3\\audio_spectra"
    print("\nConverting to spectogram with\nDimensions: "+str(length*100)+"X"+str(width*100))
    files = [f for f in listdir(path) if isfile(join(path,f))]                                      #makes list of wav files in directory
    #gray= file.open(self.directory_name + "/" + random_image_file)
    #audio_clips = os.listdir(audio_fpath)
    for audio in pbar(files):
        x, sr = librosa.load(os.path.join(path, audio))                                             #loading wav files
        plt.figure(figsize=(length, width), dpi=100)                                                #plotting 128 X 64 images 
        plt.axis('off')
        plt.axes([0., 0., 1., 1., ], frameon=False, xticks=[], yticks=[])
        S = librosa.feature.melspectrogram(y=x, sr=sr)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
        plt.savefig(os.path.join(dest, os.path.splitext(audio)[0]+'.png'), bbox_inches=None, pad_inches=0) #saving spectrogram
        plt.close()
    pbar.finish()
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', help='Source directory having audio mp3', type=str)
    parser.add_argument('--targetdir', help='Target directory to save spectograms', type=str)
    args = parser.parse_args()
    
    if args.src is None:
        print("Please specify the path to the source directory")
        exit(1)
    
    if args.targetdir is None:
        print("Please specify the path to the target directory")
        exit(1)
        
    #convertToWAV(args.src,args.targetdir)
    convertToSpectogram(args.src,args.targetdir,1.28,0.64)

if __name__ == '__main__':
    main()