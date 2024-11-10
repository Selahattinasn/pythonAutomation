# The create_python_script function creates a new python script in the current working directory, 
# adds the line of comments to it declared  by the 'comments' variable, 
# and returns the size of the new file. 

import os

def create_python_script(filename):
    comments= "Start of a new Python Programm and for all apps."
    with open(filename, "a+") as file_object : 
        file_object.write(comments)
        print(file_object.read())
        file_size=os.path.getsize(filename)
    return(file_size)

print(create_python_script("apple.py"))
