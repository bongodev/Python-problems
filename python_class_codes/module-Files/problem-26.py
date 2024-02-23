# List Comprehension: Use list comprehension to create a list of squares from 1 to 10.

# result = []

# for i in range(1, 11):
#     result.append(i * i)

result = [i * i for i in range(1, 11)]  # list comprehension

# in_string = "bongodev"

# result = [letter for letter in in_string]

print(result)
