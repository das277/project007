"""import os 
path = input("Enter your path:")
newname = input("enter the new name you want:")
converstion = os.listdir(path)
print("Old file names", converstion)
ignore = ["harry"]
count = 1 
for file in converstion:
    if file not in ignore:
        extension = os.path.splitext(file)[1]
        nayanaam = newname + str(count) + extension
        os.rename(path + "/" + file, path + "/" + nayanaam)
        count += 1

converstion = os.listdir(path)
print("Newfile name:",converstion)"""

# project by chatgpt

import os

path = input("Enter your folder path: ")
if not os.path.exists(path):
    print("Path does not exist.")
    exit()

newname = input("Enter the new base name: ")
ignore = input("Enter file names to ignore (comma-separated): ").split(",")
ignore = [i.strip() for i in ignore]

files = os.listdir(path)
print("Old file names:", files)

count = 1
for file in files:
    if file not in ignore:
        extension = os.path.splitext(file)[1]
        new_file = f"{newname}{str(count).zfill(2)}{extension}"
        os.rename(os.path.join(path, file), os.path.join(path, new_file))
        count += 1

files = os.listdir(path)
print("New file names:", files)
