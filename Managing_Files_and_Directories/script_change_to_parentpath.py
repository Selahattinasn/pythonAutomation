import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  path=os.getcwd()
  os.chdir("../")
  parent_path=os.getcwd()
#   print(path)
#   print(parent_path)
  relative_parent = os.path.join(parent_path, path)

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())