import time, os, shutil

path = input("Enter the path to the folder to be cleaned: ")
path += '/'
days = 30
seconds = time.time() - (days*24*60*60)