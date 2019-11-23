#!/usr/bin/env python3

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
import random
import argparse
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', help='Path of source directory', type=str)
    parser.add_argument('--ext', help='Extension of files to move. Default = .png', type=str)
    parser.add_argument('--target', help='Path of target directory', type=str)
    parser.add_argument('--count', help='Number of items to be moved. Default = 1', type=str)
    parser.add_argument('--all', help='Moves all files, overrides random',default=False,action='store_true')
    args = parser.parse_args()

    if args.src is None:
        print("Please specify the source directory")
        exit(1)

    if args.target is None:
        print("Please specify the target directory")
        exit(1)
    
    if args.ext is None:
        args.ext='.png'
        
    if args.count is None:
        args.count=1

    print("Moving.. ")
    
    if args.all:
        print('In args all')
        for file in os.listdir(args.src):
            print(file)
            if file.endswith(args.ext):
                shutil.move(args.src+"\\"+file,args.target+"\\"+file)
    else:
        i=1
        while i <= int(args.count):
            file_name=random.choice(os.listdir(args.src))
            shutil.move(args.src+"\\"+file_name,args.target+"\\"+file_name)
            i+=1
    
if __name__ == '__main__':
    main()
