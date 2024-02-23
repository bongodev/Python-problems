filename = "write-practice.txt"

# with open(filename, "w") as file:
#     file.write("this is bongodev!")
#     file.write("its really cold today.")

# x -> exclusive creation - fails if file already exists
# with open(filename, "x") as file:
#     file.write("this is bongodev!")
#     file.write("its really cold today.")


# write new lines also
with open(filename, "w") as file:
    file.write("this is bongodev!\n")
    file.write("its really cold today.\n")
