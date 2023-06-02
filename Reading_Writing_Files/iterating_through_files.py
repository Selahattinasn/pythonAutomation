# Files can be iterared as other python sequences; 
# like list or strings.
# This would be useful when we porzess a file line by line...

with open("siir.txt") as file:
    for line in file:
        print(line.upper())

# In the output we will see an empty line between lines: 
# Because python read the file line by line and at the end of all line 
# there will be a "new line character" . And when read() methods read the new-line character, 
# it produce an empty line

# To avoid new line caharter, use strip() method. 

with open("siir.txt") as file:
    for line in file:
        print(line.strip().upper())
