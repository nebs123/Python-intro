#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 15:48:32 2021

@author: nebiyoumetaferia
"""

import argparse
import os

def arg_parser():
    """
    Parses the arguement from the command line

    Returns
    -------
    Namespace of arguements
        

    """
    
    parser = argparse.ArgumentParser(description='Program to utilise files')
    group = parser.add_mutually_exclusive_group()
    
    group.add_argument("-c","--copy", nargs = 2, 
                        help= "copy from src to dest path " )
    group.add_argument("-ls", "--ls", nargs="?" ,const = "./", help = "list files in path (if specified)" )
    
    parser.add_argument("-r", action="store_true" , help= "option to make the copy recursive")
    return parser.parse_args()
    
def simple_copy(src, dest):
    
    
    if os.path.isdir(dest):
        if dest[len(dest)-1] == "/":
            dest= dest + src_dir_name(src)
        else:
            dest= dest + "/" + src_dir_name(src)
    try:
        with open(src, "rb") as file1:
            with open(dest, "wb") as file2:
                file2.write(file1.read())
    except IOError:
        print("Invalid src or destination file")
    

def list_file(directory):
    try:
        for  f in os.listdir(directory):
            print(f)
    except FileNotFoundError:
        print("Cannot find specified directory or File")
    except NotADirectoryError:
        print("Inputed path isn't a directory")
        
def recursive_copy(src, dest):
    
    if os.path.isfile(src):
        simple_copy(src, dest)
        
    elif os.path.isdir(src):
        if not os.path.exists(src):
            raise FileNotFoundError("can not find specified path", src)
        if os.path.isfile(dest):
            raise IOError("destination cannot be a file name")
            
        if os.path.exists(dest) and os.path.isdir(dest):
           if dest[len(dest)-1] == "/":
               dest= dest + src_dir_name(src)
           else:
               dest= dest + "/" + src_dir_name(src)
        
        os.mkdir(dest)
        
        for f in os.listdir(src):
            if src[len(src) -1] == "/":
                recursive_copy( src + f, dest)
            else:
                recursive_copy(src + "/" + f, dest)
    else:
        raise IOError("Path doesn't exist as file or directory")

def src_dir_name(path):
    
    path = path.split("/")
    if path[len(path) - 1] == "":
        return path[len(path) - 2]
    return path[len(path) - 1]

if __name__ == "__main__":
    
    args = arg_parser()
    
    if args.copy:
        if args.r:
            recursive_copy(args.copy[0], args.copy[1])
        else: 
            simple_copy(args.copy[0], args.copy[1])
        
    elif args.ls:
        #print("arguement ls", len(args.ls))
        list_file(args.ls)
    
    else:
        print("See FileUtil -h/--help for usage info")