# Find Common Elements: Create a program that finds common elements between two lists using loops.

one = [2, 5, 2, 10]
two = [6, 2, 10, 2]

# one_set = set(one)
# two_set = set(two)

# result = list(one_set.intersection(two_set))
result = []

# for i in one:
#     for j in two:
#         if i == j:
#             result.append(j)

# for i in one:
#     flag = 0
#     for j in two:
#         if i == j:
#             flag = 1
#         print(f"checking i={i} and j={j} flag={flag}")

#     if flag == 1:
#         result.append(i)

for i in one:
    if i in two:
        result.append(i)

word = "bangladesh"
print("v" in word)

# print(result)
