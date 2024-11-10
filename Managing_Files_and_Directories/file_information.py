# The functions and the OS.path module take the info provided by the operating system 
# so that we can use it in our scripts no matter what OS we're running. 
# There is a ton more functions in the OS and OSpath modules that let us work with files. 
# But don't worry, you don't have to learn them all by heart. 
# Whenever you need to do something with files, 
# it's a good idea to check the documentation and research 
# what functions are available to find the ones that you need
import os 

# We can get a lot more info about our files using functions in OS.path module

#  check how big a file is, we can use the getsize() function 
# which returns the file size in bytes.
print(os.path.getsize("safahattan.txt"))

# check when the file was last modified, 
# the getmtime() function comes in really handy.
print(os.path.getmtime("safahattan.txt"))

#  it's a timestamp. In this case specifically, it's a Unix timestamp.
#  It represents the number of seconds since January 1st, 1970.
# While Unix timestamps have a 50-year history, they're still very much present today. 
# They're used by file systems to show when a file was created, accessed, or modified. 
# They are also used in other systems like databases. 
# As an IT specialist, you're bound to run into them in your day to day. 
# But despite all of that, the number is pretty hard to make sense of. 
# We can use the datetime module to make it easier for us humans to read:
# we use fromtimestamp() method of the datetime class inside the datetime module. 
# It makes the date far easier for us to understand. 
import datetime
timestamp = os.path.getmtime("safahattan.txt")
print(datetime.datetime.fromtimestamp(timestamp))

# Another cool feature of the functions is that we can work with both relative and absolute paths. 
# In our examples, we've been using the relative file names without having to specify their full paths
# In some cases, we may need to specify exactly where the file is to work with it in our script. 
# This is where the abspath() function can help.
print(os.path.abspath("safahattan.txt"))