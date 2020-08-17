"""
Program to find files in given directory based on keyword and time stamp.
Takes a Directory and a keyword as inputs and checks if there is any file with the given condition.
Usage : python findfiles.py
"""
import os
import time

now = time.ctime()  # current date and time
print(now)
Directory = input("Please enter the path : ")
keyword = input("Please enter file extension : ")
days = int(input("How old (In days) : "))
# if the Directory ends with '/' or '\\' then add '/' with the path
if not (Directory.endswith("/") or Directory.endswith("\\")):
    Directory = Directory + "/"
# if you didn't enter any path then this will take current directory as default
if not os.path.exists(Directory):
    Directory = "."
# To find the files based on keyword and time
for files, dirs, base in os.walk(Directory):
    for file in base:
        compare = time.time() - days * 86400    # This will Subtract seven days in seconds from the current date in seconds
# This will check the files are ends with the keyword and the status of file is greater than the compare file
        if file.endswith(keyword) and os.stat(os.path.join(Directory, file)).st_mtime < compare:
            print(os.path.join(Directory, file))
