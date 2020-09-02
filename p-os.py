import os
import datetime

os.remove('path of file/directory')

os.rename('file old name', 'new name')

print(os.path.exist('file'))  # True if exist and False if it doesn't

print(os.path.getsize('file'))

os.path.getmtime('file')  # last modified

print(datetime.datetime.fromtimestamp(os.path.getmtime('file')))

print(os.path.abspath('file'))

print(os.getcwd())  # current directory

os.mkdir(directory name)

os.chdir(directory name)

os.rmdir(directory name)  # remove only if directory is empty

print(os.listdir(directory name))

os.isdir(name)
