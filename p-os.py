import os
import datetime

os.remove('path of file/directory')

os.rename('file old name', 'new name')

os.path.exist('file')  # True if exist and False if it doesn't

os.path.getsize('file')

os.path.getmtime('file')  # last modified

datetime.datetime.fromtimestamp(os.path.getmtime('file'))

os.path.abspath('file')

os.getcwd()  # current directory

os.mkdir(directory name)

os.chdir(directory name)

os.rmdir(directory name)  # remove only if directory is empty

os.listdir(directory name)

os.isdir(name)

os.environ  # A Dictionary of Environment Variables
