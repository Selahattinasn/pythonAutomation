# Files can be iterared as other python sequences; 
# like list or strings.
# This would be useful when we porzess a file line by line...
siir="C:\\Users\\karakaya\\Desktop\\Agenda\\pythonAutomation\\Reading_Writing_Files\\siir.txt"
with open(siir) as file:
    for line in file:
        print(line.upper())

# In the output we will see an empty line between lines: 
# Because python read the file line by line and at the end of all line 
# there will be a "new line character" . And when read() methods read the new-line character, 
# it produce an empty line

# To avoid new line caharter, use strip() method. 

with open(siir) as file:
    for line in file:
        print(line.strip().upper()) #we use strip to remove the newline character, we get the output without empty lines,



# Another way we can work with the contents of the file is to read the file lines into a list. 
# Then, we can do something with the lists like sort contents. 
# To do that, we open the file and use the.readlines method. 

file= open(siir)

lines = file.readlines()
print(type(lines)) # lines varible is actually a list sequence. 
file.close() # we closed the fule object but we have already a python_list, consist of lines of the text. 

print(lines)
lines.sort()
print(lines)

# Escape characters: \n  \t  
## !!!! f a file is just a few kilobytes like in our example here, 
# it's fine to read it and process it completely in memory. 
# But for large files, like the big log file of hundreds and hundreds of megabytes of data, 
# it's more efficient to process it line by line.