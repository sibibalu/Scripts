import os
import time

now = time.ctime()
filecompare = time.time() - 7 * 86400
print(now)
Directory = input("Please enter the path : ")
keyword = input("Please enter file extension : ")
if not (Directory.endswith("/") or Directory.endswith("\\")):
    Directory = Directory + "/"
if not os.path.exists(Directory):
    Directory = "."
for files, dirs, base in os.walk(Directory):
    for file in base:
        #filestamp = os.stat(os.path.join(Directory, file)).st_mtime
        if file.endswith(keyword): #  and filestamp < filecompare:
            print(file)
