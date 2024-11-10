# Now we remove the guests that have checked out already. 
# There are several ways to do this, 
# however, the method we will choose for this exercise is outlined as follows:

# Open the file in "read" mode.
# Iterate over each line in the file and put each guest's name into a Python list.
# Open the file once again in "write" mode.
# Add each guest's name in the Python list to the file one by one.

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)
