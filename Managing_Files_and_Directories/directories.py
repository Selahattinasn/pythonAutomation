# as with files, Python provides a bunch of different functions that let us create, delete and browse the contents of directories.
import os

# to check the current directory use getcwd() function.
print(os.getcwd())

# to make new-directory use mkdir("sample") function.
os.mkdir("sample")

# to change the directory use chdir("sample") function.
os.chdir("sample")
print(os.getcwd())

## to change the directory use rmdir("sample") function.
os.rmdir("sample")
# but the rmdir function will only work if the directory is empty. 
# If we try to remove a directory that has files in it, we get an error. 
# We need to first delete all the files and sub-directories in that directory 
# before we can actually remove it 
# but how can we find out what contents are in that directory?

# The os.listdir function returns a list of all the files and sub-directories in a given directory. 
print(os.listdir("sample"))

# So we've got a list of strings. 
# Since they're just strings, we don't know if they're directories or files. 
# To find out what they are, we can use functions like os.path.isdir() 
# but before we look at how that works. 
# See how the list contains just file names. 
# If we want to know whether one of these files is a directory, 
# we need to use os.path.join() to create the full path. 
# Let's see all of this in action now.
website=['images', 'index.html', 'ifavicon.ico']
os.listdir("website")   
dir="website"
for name in os.listdir(dir):
    fullname=os.path.join(dir, name)
    if os.path.isdir(fullname):  # we use that full name to call os.path.isdir to check if it's a directory or a file
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

# os.path.join() seems to just add a slash between two strings. 
# Well, the join function let's us be independent from the operating system again. 
# In Linux and MacOS, the portions of a file are split using a forward slash. 
# On Windows, they're split using a backslash. 
# By using the os.path.join function instead of explicitly adding a slash, 
# we can make sure that our scripts work with all operating systems. 
# It's another one of those handy little tools that help us avoid errors 
# when working on different platforms.