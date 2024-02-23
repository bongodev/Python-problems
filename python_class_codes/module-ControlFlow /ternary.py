# ternary operators

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter third number: "))

# min = b

# if a < b:
#     min = a

# [on_true] if [expression] else [on_false]
# min = a if a < b else b

# print('minimum is: ', min)

# print('Both a and b are equal' if a == b else 'they are not the same')

# we need to return the smallest number from (x, y)
# [b < a] -> [0]
# (a, b)[b < a]

# tuples
# print((b, a) [1 if a < b else 0])

# checkin for 3 numbers
min = a if a < b and a < c else b if b < c else c
print(min)
# print((2, 3)[0])
