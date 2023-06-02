with open("siir.txt", "r+") as file:
    file.write("          Mehmet Akif Ersoy")
    file.read()

# write() method is user´d to write a line to the text. 
# to use write() method we must use also a second parameter:
# "w" , because the by default mode (file-permission) of open-function is "r" read-only;
# "w" must be passe to enabel write-mode.
# "w" enables overwriting
# "w" means write.only: we cant read the content in this mode . "w" means we overwrite the content. 

# "a" mode enables adding content to file.

# "r+" mode is "read+write" mode

# "r" read-only-mode  (default mode for open()-function)
# "w" write-only-mode
# "a" append-mode
# "r+" read+write-mode

# !!!  f you open a file for writing and the file already exists, 
# the old contents will be deleted as soon as the file is opened
# Thats why use the rigt mode for the file
