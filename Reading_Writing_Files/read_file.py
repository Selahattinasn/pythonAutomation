
# Python gives us file objects which we can use to read and write to files
# What we're doing here is creating a new file object and assigning it to a variable called File. 
# The parameter we've passed to the open function is the name of the file we want to open. 
# In this case, we're assuming the file we want to read is in the same directory as a script we're running
# but we can just as easily pass an absolute paths to open a file in a different directory. 
# When we open a file, like we're doing in this example, the operating system checks 
# that we have permissions to access that file and then gives our code a file descriptor. 
# This is a token generated by the OS that allows programs to do more operations with the file. 
#In Python, this file descriptor is stored as an attribute of the files object. 
# The file object gives us a bunch of methods that we can use to operate with the file. 
# Now, with this file object, we can read the contents of the file and print them to the
siir="C:\\Users\\karakaya\\Desktop\\Agenda\\pythonAutomation\\Reading_Writing_Files\\siir.txt"
file=open(siir)
print(file.readline()) # Here we've used the readline method. It lets us read a single line of a file. 
print(file.read()) # read method, which reads from the current position until the end of the file instead of just one line.

file.close()

# to automaticall close the obje use the "with" keyword.
with open(siir) as file_line:
    print(file_line.read())

# It's a good idea to close files after you've opened them for a few reasons. 
# First, when a file is opening your script, 
# your file system usually lock it down and so no other programs or scripts can use it 
# until you're finished. 
# Second, there's a limited number of file descriptors 
# that you can create before your file system runs out of them. 
# Although this number might be high, 
# it's possible to open a lot of files and deplete your file system resources. 
# This can happen if we're opening files in a loop, for example. 
# Third, leaving open files hanging around can lead to race conditions 
# which occur when multiple processes try to modify and read from one resource at the same time 
# and can cause all sorts of unexpected behavior. 
# No one wins in a race condition.