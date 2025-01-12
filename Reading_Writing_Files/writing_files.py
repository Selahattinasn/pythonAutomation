with open("hello.py", "w") as hello: # 
    hello.write("print('Selamun aleykum sakirt')")
#he second argument to the open method is new though. 
# So what does the w mean? 
# File objects can be opened in several different modes. 
# A mode is similar to a file permission. 
# It governs what you can do with the file you've just opened. 
# By default, the open function uses the r mode, which stands for read only. 
# You get an error if you try to write to a file opened in read only mode. Since read only is the default, 
# we don't have to pass the R as a second argument when we just want to read the file.#


with open("siir.txt", "a+") as file:
    file.write("          Mehmet Akif Ersoy")
    file.read()

# write() method is user´d to write a line to the text. 
# to use write() method we must use also a second parameter:
# we canr read a file in "w" (write-only) mode. 

# If you want to add content to a file that already exist, you can do that by using other modes like a for appending content at the end of an existing file. 
# Or r+ for read-write mode, where you can both read contents and overwrite it.

# !!!  if you open a file for "w" writing and the file already exists, 
# the old contents will be deleted as soon as the file is opened
# Thats why use the rigt mode for the file

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

