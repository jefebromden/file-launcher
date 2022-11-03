#!/usr/bin/env python3 -X pycache_prefix='mycachefolder'
# File name: launcher.py
# Description: Simple script to list files on a folder and run the selected file in its default application.
# Author: Agustin Ayala
# Date: 01-11-2022
import platform,os,tempfile
import subprocess,argparse

import pandas
from rich.console import Console
from rich.table import Table

PLATFORM = platform.uname().system
HOME= os.path.expanduser('~')
TABLE_TITLE = "Wendy's Files"

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

def defaultMethodOld(listing,selected):
    path = listing.iloc[selected]['Path']
    openFile(path)

def listOptionsOld(directory=None):
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

def defaultMethod(listing,selected):
    path = listing[selected][1]
    openFile(path)

def listOptions(directory=None):
    listing = []
    columns = {
        'Name': 'cyan',
        'Path': 'magenta'
    }
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

def createTable(header,rows,title=TABLE_TITLE):
    table = Table(title=title)
    table.add_column('Index',style='green')
    for name,color in header.items():
        table.add_column(name,style=color)

    index = 0
    for item in rows:
        table.add_row(str(index),item[0],item[1])
        index += 1

    return table

def main():
    args       = parse_arguments()
    directory  = args.d
    exitOption = 'e'
    inputMsg   = 'Select a file to open ("{eo}" to exit): '

    while True:
        listing,columns = listOptions(directory)
        #listing         = pandas.DataFrame(
        #                    listing,
        #                    columns=columns)
        #print(listing)
        table = createTable(columns,listing)
        console = Console()
        console.print(table)
        print()
        selected        = input(inputMsg.format(eo=exitOption))

        try:
            selected = int(selected)
            # if selected in listing.index.to_list():
            if selected < len(listing):
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
