import os

path=os.getcwd()
print(path)
os.chdir("../")
parent_path=os.getcwd()
print(parent_path)