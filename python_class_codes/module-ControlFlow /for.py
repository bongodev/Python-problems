# syntax

# for i in range(1, 5):
#     print(i)

fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)


# make uppercase
# another = []
# for fruit in fruits:
#     fruit = fruit.upper()
#     another.append(fruit)

# print("upper", another)
# print("fruits", fruits)


# reverse a string - exercise
# input = "hello"
# reversed = ""

# for letter in input:
#     # print("adding ", letter)
#     reversed = reversed + letter

# print(reversed)


# descending w/ range
# range synteax: range(start, stop, step)
# for i in range(10, 1, -2):
#     print(i)

# comparison with C

# for (i = 5; i < n; i+=2){
#     printf("%d\n", i);
# }
# equivalent python
# for i in range(5, n, 2):
#     print(i)


# input = "good"
# reversed = ""
# print(input)
# for i in range(len(input) - 1, -1, -1):
#     print("now adding: ", input[i])
#     reversed = reversed + input[i]

# print(reversed)

building = [
    ["G1", "G2", "G3", "G4"],
    ["A1", "A2", "A3", "A4"],
    ["B1", "B2", "B3", "B4"],
]  # 2D matrix - 3 x 4

# list of list - individual items are also a list

# floors = 3
# apartments = 4

# for i in range(floors):
#     print("now in floor: ", i)
#     for j in range(apartments):
#         print("knocking on apartment: ", building[i][j])

for floor in building:
    print("now: ", floor)
    for apartment in floor:
        print("knocking on: ", apartment)


# floor1 = ["G1", "G2", "G3"]
# floor2
# [floor1, floor2, floor3]

# [
#     [[1, 2], [3, 4]],
#     [[9, 10], [11, 12]],
#     [[5, 6], [7, 8]],
#     [[13, 14], [15, 16]],
# ]
