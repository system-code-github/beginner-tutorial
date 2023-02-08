# -*- coding: UTF-8 -*-

# import models
import time as t
import os as o
import pygame as p

# define some variables

sf = "snd.wav" # sound file

# define some functions

# open the documents

def openFile(): # open file function
    for i in range(6571): # traversing documents
        fn = "out\\" + str(i) + ".txt"
        with open(fn, 'r', encoding= 'utf-8') as f:
            dat = f.read()
            dlist.append(dat)
# start printing

def run():
    # use 'pygame' module to play the music
    p.mixer.init()
    p.mixer.music.load(sf)
    p.mixer.music.play()

    for j in range(6571):
        i = int((j/6571)*1000)
        t.sleep(0.03) # sleep a few time to prevent jamming
        print(dlist[j]) # print main text
        print(f"Frame#{i}") # print frame text

t.sleep(3)
o.system('cls')

if __name__ == '__main__':
    dlist = []

# run the functions
openFile()
run()