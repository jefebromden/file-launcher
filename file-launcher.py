#!/usr/bin/env python3 -X pycache_prefix='mycachefolder'
# File name: launcher.py
# Description: Simple script to list files on a folder and run the selected file in its default application.
# Author: Agustin Ayala
# Date: 01-11-2022
import platform,os,tempfile
import subprocess,argparse

import pandas

PLATFORM = platform.uname().system
HOME= os.path.expanduser('~')

def parse_arguments():
    """Command line arguments parser."""
    parser = argparse.ArgumentParser(description='List files on a given directory and open the selected file with its default application.')
    parser.add_argument(
        '-d', metavar='directory',
        type=str, default=HOME,
        help='Directory to list. Defaults to user HOME directory.')

    args = parser.parse_args()

    return args

def quit():
    print('Have a nice day!')
    raise SystemExit()

def usage():
    print("""Choose a number inside the range of the options listed.""")

def invalidOption(option,msg=None):
    if not msg:
        msg = '{op} is out of range.'
    print()
    print(msg.format(op=option))
    usage()
    print()

def openFile(path):
    if PLATFORM == 'Linux':
        command = 'xdg-open "{path}"'
    elif PLATFORM == 'Windows':
        command = 'start "" "{path}"'
    else:
        print(f'{PLATFORM} platform is not supported.')
        raise SystemExit()

    if os.path.isfile(path):
        open_file = command.format(path=path)
        subprocess.call(open_file,shell=True)
    else:
        print(f'{path} is not a file')

def defaultMethod(listing,selected):
    path = listing.iloc[selected]['Path']
    openFile(path)

def listOptions(directory=None):
    listing = []
    columns = ['Name','Path']
    if not directory:
        directory = HOME

    if os.path.isdir(directory):
        directory = os.path.abspath(directory)
        for item in os.listdir(directory):
            path = os.path.join(directory,item)
            if os.path.isfile(path):
                # Don't list hidden files
                if item[0] != '.':
                    listing.append((item,path))

    return listing,columns

def main():
    args       = parse_arguments()
    directory  = args.d
    exitOption = 'e'
    inputMsg   = 'Select a file to open ("{eo}" to exit): '

    while True:
        listing,columns = listOptions(directory)
        listing         = pandas.DataFrame(
                            listing,
                            columns=columns)
        print(listing)
        print()
        selected        = input(inputMsg.format(eo=exitOption))

        try:
            selected = int(selected)
            if selected in listing.index.to_list():
                defaultMethod(listing,selected)
            else:
                invalidOption(selected)
        except ValueError as ve:
            if selected.lower() == 'e':
                quit()
            else:
                invalidOption(selected,msg='{op} is not an integer.')

if __name__ == '__main__':
    if PLATFORM in ['Linux','Windows']:
        main()
    else:
        print(f'{PLATFORM} platform is not supported.')
        raise SystemExit()
