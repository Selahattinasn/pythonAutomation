
file_obje=open("siir.txt")

print(file_obje.readline())
print(file_obje.read())

file_obje.close()

# to automaticall close the obje use the "with" keyword.
with open("siir.txt") as file_object:
    print(file_object.read())

