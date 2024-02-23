# file_object = open(filename, 'mode')
# file_object.close()

# mode = 'r' -> read, 'w' -> write, 'a' -> append

with open("example-file.txt", "w") as file:
    file.write("Hello world!")

with open("example-file.txt", "r") as file:
    print(file.read())

with open("example-file.txt", "a") as file:
    file.write("Added this part!")

with open("example-file.txt", "r") as file:
    print(file.read())

# with open("example-file.txt", "w") as file:
#     file.write("new write!")

# with open("example-file.txt", "r") as file:
#     print("INSIDE!!")
#     print(file.read())

# print("OUTSIDE!!")
# print(file.read()) # error because file closed

# file = open("example-file.txt", "r")
# # print(file.read())
# for line in file:
#     letters = [letter for letter in line]
#     print(letters)
# file.close()
