#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', help='Path of source directory', type=str)
    parser.add_argument('--target', help='Path of target directory', type=str)
    args = parser.parse_args()

    if args.src is None:
        print("Please specify the source directory")
        exit(1)
        
    if args.target is None:
        print("Please specify the target directory")
        exit(1)
        
    lines = open(args.src, 'r').readlines()
    output = open(args.target, 'w')

    for line in sorted(lines, key=lambda line: line.split(',')[0]):
        output.write(line)

    output.close()
    
if __name__ == '__main__':
    main()