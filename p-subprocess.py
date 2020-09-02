import subprocess

subprocess.run(["date"], shell=True)

result = subprocess.run(["date"], shell=True, capture_output=True)
result.returncode
# 0
result.stdout
# b'The current date is: Wed 09/02/2020 \r\nEnter the new date: (mm-dd-yy) '
result.stdout.decode()
# The current date is: Wed 09/02/2020
# Enter the new date: (mm-dd-yy)

"ERROR"
# subprocess.run(["dir", "hello.txt"])
# returncode = 1

# result = subprocess.run(["del", "hello.txt"], capture_output=True)
# result.returncode
# # 1
# result.err
