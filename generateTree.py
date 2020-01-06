### We start with some kind of regex shit. I need to learn how to do 
### regex shit. Whoops
import re
import sys

def main():
    texDoc = open('treeDoc.txt', 'w') #Maybe make this a legit tex file
    texString = readtree(argv[1])
    texDoc.write(texString)

def readtree(tree):    
    