# testing with r+
filename = "demo.txt"

with open(filename, "r+") as file:
    file.write("new line!\n")
