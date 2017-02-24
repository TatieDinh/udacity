import os

def changename(filename):
    os.listdir(r"F:\udacity\name")
    os.chdir(r"F:\udacity\name")
    savepath = os.getcwd()
    print(savepath) 
    os.rename(filename, "comment.txt")  

changename("co.txt")
