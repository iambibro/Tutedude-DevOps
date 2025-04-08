# 3.Write to a File
# Write a program to create a text file and write some content to it.

# Using file functions like write and open.

with open("write_to_file.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a text file.\n")
