import os
os.remove("novel.txt")

os.rename("siir.txt", "safahattan.txt")

# we can check if a file exisists wit path submodule nd exists() method.
os.path.exists("safahattan.txt")