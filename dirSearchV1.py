# -*- coding: utf-8 -*-
import time
import tkinter as tk
import os
rootdir = '/'
#Open a gui with a text box and button that accepts input
#Request name of file that user is looking for, then press the find file button to call the menu function
#menu determines whether youre looking for a file or a directory, defaults to directory with no .txt or other . extention
#home = os.path.expanduser("~")
#print(home)
#exists supposed to check if file/directory exists before sending
#it to folderFinder or fileFinder
def menu():
    filetofind = winput.get()
#    pathtofind = os.path.join(rootdir, filetofind)
    if '.' in filetofind:
        exists = os.path.isfile(filetofind)
#        if exists == True:
        print('\nSearching for file')
        result = fileFinder(filetofind)
#        else:
#            print(pathtofind)
#            result = 'File does not exist. Enter another file'
    elif '.' not in filetofind:
#        exists = os.path.isdir(filetofind)
#        if exists == True:
        print('\nSearching for folder')
        result = folderFinder(filetofind)
#        else:
#            result = 'Directory does not exist. Enter another folder name'
    print(result)
def folderFinder(targetdir):
    counter = 0
    for path, dirname, fname in os.walk(rootdir):
        for dname in dirname:
            counter += 1
#            print(path, dname)
            if dname == targetdir:
                parentpath = os.path.join(path, dname)
                print(counter)
                return f'File found!\n File path: {parentpath}\n\t Folder Name:{dname}'



def fileFinder(targetf):
    counter = 0
    for path, dirname, fname in os.walk(rootdir):
        counter += 1
        for name in fname:
#            print(path, name)
            if name ==  targetf:
                print(counter)
                parentpath = os.path.join(path, name)
                return f'File found!\n File path: {parentpath}\n\t File Name: {name}'


if __name__ == '__main__':
    t1= time.time()
    window = tk.Tk()
    wtitle = tk.Label(text="Welcome to the Directory searcher!\n Please enter the file or directory you'd like to search for", width=50, height=10)
    winput = tk.Entry()
    wbutton = tk.Button(text="Find File", width=10, height=2, bg="#42e3f5", command=menu)
    wexit = tk.Button(text= 'Exit', width=10, height=2, bg='#ed2f2f', command=exit)
    wtitle.pack()
    winput.pack()
    wbutton.pack()
    wexit.pack()
    print(rootdir)
    print(input("this fix?"))
