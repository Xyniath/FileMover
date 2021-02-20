#TODO test and add support for absolute file paths and files & directories that are not in the working directory

import os
from os import path
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_list", help="file path of file list")
parser.add_argument("-m", "--makefolder", action='store_true',
                    help="Specifies if you want the folder to be created if it doesnt already exist, and name it")
parser.add_argument("destination", help="destination for files")
args = parser.parse_args()

working_directory = os.getcwd()

intro_art = """
>  ______   _____   _        ______   __  __    ____   __      __  ______  <
> |  ____| |_   _| | |      |  ____| |  \/  |  / __ \  \ \    / / |  ____| <
> | |__      | |   | |      | |__    | \  / | | |  | |  \ \  / /  | |__    <
> |  __|     | |   | |      |  __|   | |\/| | | |  | |   \ \/ /   |  __|   <
> | |       _| |_  | |____  | |____  | |  | | | |__| |    \  /    | |____  <
> |_|      |_____| |______| |______| |_|  |_|  \____/      \/     |______| <
                                                                           <
                                                                         
                        ={   BY >XYNIATH   <}=                
                                                        
                          Twitter : >@Xyniath<                  
                       Site : >xyniath.github.io<               
                                                                         """
green = "\033[1;32m"
cyan = "\033[0;36m"
red = "\033[1;31m"
clear = "\033[0m"

load = "[>$<] ".replace(">", green).replace("<", clear)
err = "[>-<] ".replace(">", red).replace("<", clear)
intro = intro_art.replace(">", cyan).replace("<", clear)


print(intro)


def does_file_exist(file_name):
    if path.exists(file_name):
        os.rename(working_directory + "/" + file_name, working_directory + "/" + args.destination + "/" + file_name)
    else:
        print("File: '" + file_name + "' not found.")


def main():
    if args.makefolder:
        if path.exists(args.destination):
            directory_exists = "Directory >" + args.destination + "< already exists."
            print(directory_exists.replace(">", red).replace("<", clear))
            sys.exit()
        else:
            print("Creating directory: " + args.destination)
            os.mkdir(working_directory + "/" + args.destination)

    with open(str(args.file_list)) as fileList:
        for file in fileList:
            stripped = file.rstrip()
            does_file_exist(stripped)


if __name__ == "__main__":
    main()
