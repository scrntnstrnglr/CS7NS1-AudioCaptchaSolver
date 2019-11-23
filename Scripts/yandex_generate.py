"""
Generating captcha mp3 audio files.
python Scripts/generate_audio.py --count 10 --symbols Symbols/symbols.txt --length 8 --tts gtts --targetdir C:\\Users\\SIDDHARTHA\\Downloads\\captchas\\audio\\gtts
"""

from gtts import gTTS 
import tts.sapi
import os
import random
import argparse
from progressbar import ProgressBar
from os.path import join, dirname
from yandex_speech import TTS

def numbersAreTogether(text):
    for i in range(0,len(text)-1):
        if text[i].isdigit() and text[i+1].isdigit():
            return True
    return False
    
def formRandomText(length,symbols):
    s=''
    for i in range(length):
        chr = str(symbols[random.randint(0,len(symbols)-1)])
        if len(s)>0:
            while s[len(s)-1].isdigit() and chr.isdigit():
                chr = str(symbols[random.randint(0,len(symbols)-1)])
        s = s + chr  #selecting random characters from symbols file of length mentioned
    return s


def generate(count,length,symbols,targetdir,service):
    print("\nGenerating...\ncount: ",count,"\nlength: ",length,"\ntts: ",service,"\n")
    pbar=ProgressBar()
    for j in pbar(range(count)):
        sent=formRandomText(length,symbols)
        mytext = sent
        language = 'en'
        
        
            

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--targetdir', help='Target directory to save generated audios', type=str)
    parser.add_argument('--count', help='Number of audios files', type=int, default=100)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    parser.add_argument('--length', help='Length of captchas', type=int, default=5)
    parser.add_argument('--tts', help='Length of captchas', type=str, default='gtts')
    args = parser.parse_args()
    
    if args.targetdir is None:
        print("Please specify the path to the target directory")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)
        
    if args.count is None:
        print("Defaulting count to 100")
        
    if args.length is None:
        print("Defaulting length to 5")
        
    if args.tts is None:
        print("Defaulting TTS to Google text to Speech service.")

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    symbols_file.close()
    
    generate(args.count,args.length,captcha_symbols,args.targetdir,args.tts)
    
if __name__ == '__main__':
    main()
    
    
    