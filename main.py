import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_list", help="file path of file list")
parser.add_argument("-t", "--timeout", type=int, help="timeout in seconds (default 20)")
parser.add_argument("-m", "--makeFolder", type=str,
                    help="Specifies if you want the folder to be created if it doesnt already exist, and name it")
args = parser.parse_args()

path = os.getcwd()

introart = """
>  ______   _____   _        ______   __  __    ____   __      __  ______  <
> |  ____| |_   _| | |      |  ____| |  \/  |  / __ \  \ \    / / |  ____| <
> | |__      | |   | |      | |__    | \  / | | |  | |  \ \  / /  | |__    <
> |  __|     | |   | |      |  __|   | |\/| | | |  | |   \ \/ /   |  __|   <
> | |       _| |_  | |____  | |____  | |  | | | |__| |    \  /    | |____  <
> |_|      |_____| |______| |______| |_|  |_|  \____/      \/     |______| <
                                                                           <
                                                                         
                           ={>   BY XYNIATH   <}=                
                                                        
                            Twitter : >@Xyniath<                  
                         Site : >xyniath.github.io<               """
green = "\033[1;32m"
red = "\033[1;31m"
clear = "\033[0m"

load = "[>$<] ".replace(">", green).replace("<", clear)
err = "[>-<] ".replace(">", red).replace("<", clear)
intro = introart.replace(">", green).replace("<", clear)

print(intro)


def does_file_exist(file_path):
    if os.path.exists(file_path):
        print(file_path)
    else:
        print(file_path)


with open(str(args.file_list)) as fileList:
    for file in fileList:
        does_file_exist(file)
