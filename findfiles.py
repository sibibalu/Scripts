import os
import time

now = time.ctime()
print(now)
Directory = input("Please enter the path : ")
keyword = input("Please enter file extension : ")
if not (Directory.endswith("/") or Directory.endswith("\\")):
    Directory = Directory + "/"
if not os.path.exists(Directory):
    Directory = "."
for files, dirs, base in os.walk(Directory):
    for file in base:
        compare = time.time() - 7 * 86400
        if file.endswith(keyword) and os.stat(os.path.join(Directory, file)).st_mtime < compare:
            print(os.path.join(Directory, file))
