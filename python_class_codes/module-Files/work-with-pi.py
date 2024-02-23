filename = "pi.txt"
pi_string = ""

# rstrip, lstrip, strip - remove whitespaces

with open(filename, "r") as file:
    for line in file:
        stripped_line = line.strip()
        print(f"this line: '{line}'")
        print(f"stripped line '{stripped_line}'")
        pi_string += stripped_line

print(pi_string)

decimal_index = pi_string.index(".")
# print("index:", decimal_index)

print(len(pi_string[decimal_index + 1 :]))
