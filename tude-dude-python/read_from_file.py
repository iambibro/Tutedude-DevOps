# 4. Read from a File
# We used open in read mode and file.read to read and print to display.

with open("write_to_file.txt", "r") as file:
    content = file.read()
    print(content)