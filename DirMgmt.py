import os

Directory = input("Please enter the Dir Name : ")
pathf = os.path.join(os.getcwd(), Directory)

if Directory in (os.listdir()):
    print("Directory '%s' Already Exist" % Directory)
    while True:
        dele = input("Do you want to rename the Directory '%s' (y/n): " % Directory).lower()
        if dele[0] == 'y':
            os.renames(pathf, "old-" + Directory)
            print("Directory '%s' renamed" % Directory)
            break
        elif dele[0] == 'n':
            print("Ok")
            break
        else:
            print("input %s y or %s n")
else:
    Mode = int(input("Please enter the permission : "), 8)
    os.mkdir(pathf, Mode)
    print("Directory '%s' created" % Directory)