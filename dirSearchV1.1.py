# -*- coding: utf-8 -*-
import time
import tkinter as tk
import os
rootdir = '/'
#Open a gui with a text box that accepts input, a button, and a dropdown menu
#Request name of file that user is looking for, then press the find file button to call the menu function
#menu determines whether youre looking for a file or folder based on
#dropdown menu selection in UI

#home = os.path.expanduser("~")
#print(home)
def menu():
    ddown = wdropdowntext.get()
    print(f'Searching for {ddown}')
    filetofind = winput.get()
    pathtofind = filetofind
    if ddown == "Select what you want to search for":
        result = 'Please select an option from the dropdown menu'
    elif ddown == 'File':
#        exists = os.path.isfile(pathtofind)
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
def folderFinder(targetdir):
    counter = 0
    for path, dirname, fname in os.walk(rootdir):
        for dname in dirname:
            counter += 1
#            print(path, dname)
            if dname == targetdir:
                parentpath = os.path.join(path, dname)
                print(f'Folder found after {counter} directories searched')
                return f'File found!\n File path: {parentpath}\n\t Folder Name:{dname}'
    return 'Folder not found'


def fileFinder(targetf):
    counter = 0
    for path, dirname, fname in os.walk(rootdir):
        counter += 1
        for name in fname:
#            print(path, name)
            if name ==  targetf:
                print(f'File found after {counter} directories searched')
                parentpath = os.path.join(path, name)
                return f'File found!\n File path: {parentpath}\n\t File Name: {name}'
    return 'File not found'

if __name__ == '__main__':
    t1= time.time()
    window = tk.Tk()
    wtitle = tk.Label(text="Welcome to the Directory searcher!\n Please enter the file or directory you'd like to search for", width=50, height=10)
    winput = tk.Entry()
    wbutton = tk.Button(text="Find File", width=10, height=2, bg="#42e3f5", command=menu)
    wexit = tk.Button(text= 'Exit', width=10, height=2, bg='#ed2f2f', command=exit)
    wdropdowntext = tk.StringVar()
    wdropdowntext.set("Select what you want to search for")
    wdropdown = tk.OptionMenu(window, wdropdowntext, "File", "Folder")
    wdropdown.pack()
    wtitle.pack()
    winput.pack()
    wbutton.pack()
    wexit.pack()
    window.mainloop()
    print(rootdir)
