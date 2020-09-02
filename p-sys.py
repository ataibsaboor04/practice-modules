#! python
import sys
import os
"""
        To check exit status of the last executed command
        In windows:
        echo %errorlevel%
        In Linux:
        echo $?

"""

print(sys.argv)

# if we run this file in cmd like this:
# p-sys.py
# then it will print:
# ['E:\\Python Programs\\Practice\\p-sys.py']

# similarly

# python p-sys.py
# ['p-sys.py']

# python p-sys.py 2 a lamp
# ['p-sys.py', '2', 'a', 'lamp']

"""
                            CREATE FILE
"""
filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("New file created\n")

else:
    print(f"Error, the file {filename} already exists!")
    sys.exit(1)
