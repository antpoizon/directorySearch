# -*- coding: utf-8 -*-
import time
import tkinter as tk
import os
import sys
from sys import platform
import hashlib
print(platform)
if platform == 'linux' or platform == 'linux2':
    rootdir = '/'
elif platform == 'win32' or platform == 'cygwin' or platform == 'msys':
    rootdir = 'C:\\'
elif platform == 'darwin':
    rootdir = '/'
#Open a gui with a text box that accepts input, a button, and a dropdown menu
#Request name of file that user is looking for, then press the find file button to call the menu function
#menu determines whether youre looking for a file or folder based on
#dropdown menu selection in UI

#home = os.path.expanduser("~")
#print(home)
def menu():
    os.chdir(rootdir)
    print(os.getcwd())
    ddown = wdropdowntext.get()
    print(f'Search declared as: {ddown}')
    filetofind = winput.get()
    pathtofind =  filetofind
    print(f'path:{pathtofind}')
    if ddown == "Select what you want to search for":
        result = 'Please select an option from the dropdown menu'
    elif ddown == 'File':
#        exists = os.path.exists(pathtofind)
#        if exists == True:
        print('\nSearching for file')
        result = fileFinder(pathtofind)
#        else:
#            print(pathtofind)
#            result = 'File does not exist. Enter another file'
    elif ddown == 'Folder':
#        exists = os.path.isdir(pathtofind)
#        if exists == True:
        print('\nSearching for folder')
        result = folderFinder(filetofind)
    elif filetofind == '': #ensures no blank string is inputted
        result = 'Please enter a file or folder name'
    print(result)
#    print(f'Searching for {ddown} took {t3} seconds')
def folderFinder(targetdir):
    dirlist = []
    t1 = time.time()
    counter = 0
    for path, dirname, fname in os.walk(rootdir):
        for dname in dirname:
            counter += 1
#            print(path, dname)
            if dname == targetdir:
                parentpath = os.path.join(path, dname)
                print(f'\nFolder found after {counter} directories searched')
                dirlist.append(parentpath)
                print(f'Folder found!\n Folder path: {parentpath}\n\t Folder Name:{dname}')
    if dirlist == []:
        return 'Folder not found'
    else:
        return dirlist

def fileFinder(targetf):
    flist = []
    counter = 0
    for path, dirname, fname in os.walk(rootdir):
        counter += 1
        for name in fname:
#            print(path, name)
            if name ==  targetf:
                print(f'\nFile found after {counter} directories searched')
                parentpath = os.path.join(path, name)
                print(f'File found!\n File path: {parentpath}\n\t File Name: {name}')
                flist.append(parentpath)
    if flist == []:
        return 'File not found'
    else:
        return flist

def md5Check():
    flist = []
    md5list = []
    badlist = []
    for path, dirname, fname in os.walk(rootdir):
        for name in fname:
#            flist.append(os.path.join(path, name))
            filetype = os.access(os.path.join(path, name), os.R_OK)
            item = os.path.join(path, name)
            try:
                ft = open(item, 'rb')
                ft.close()
                if '/sys/kernel' in item:
                    continue
                if filetype== True:
                    with open(item, 'rb') as f:
                         md5obj = hashlib.md5()
                         fdata = f.read()
                         md5obj.update(fdata)
                         md5list.append(md5obj.hexdigest())
                         print(f'try: {item}')
            except (PermissionError, FileNotFoundError, OSError, IOError):
                badlist.append(item)
                print(f'except:{item}')
    print(len(flist))
#    print(badlist)

#    print(flist)
#    print(md5list)
if __name__ == '__main__':
    window = tk.Tk()
    wtitle = tk.Label(text="Welcome to the Directory searcher!\n Please enter the file or directory you'd like to search for", width=50, height=10)
    winput = tk.Entry()
    wbutton = tk.Button(text="Find", width=10, height=2, bg="#42e3f5", command=menu)
    wexit = tk.Button(text= 'Exit', width=10, height=2, bg='#ed2f2f', command=exit)
    wdropdowntext = tk.StringVar()
    wdropdowntext.set("Select what you want to search for")
    wdropdown = tk.OptionMenu(window, wdropdowntext, "File", "Folder")
    wmd5button = tk.Button(text="Search md5 (WIP)", width=10, height=2, bg='#ba1cbd', command=md5Check)
    wdropdown.pack()
    wtitle.pack()
    winput.pack()
    wbutton.pack()
    wmd5button.pack()
    wexit.pack()
    window.mainloop()
    print(rootdir)
