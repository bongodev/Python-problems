# numbers = [5, 8, 3, 10, 2]

# words = ["hello", "world", "python"]

# print(sorted(numbers, reverse=True))

# numbers = [10, 1, 3, 2]
# numbers_dict = {0: 10, 1: 1, 2: 3, 3: 2}

# numbers[0]
# dict["kafka"]

# dict = {"kafka": 10, "hemmingway": 1, "orwell": 3, "heidegger": 2}
# print(dict.items())

# keys = sorted(dict.keys())
# # print("keys sorted ", keys)
# # print("sorting dictionary by key")

# empty_dict = {}
# for key in keys:
#     print(f"now adding key {key} value {dict[key]}")

#     empty_dict[key] = dict[key]

# print(empty_dict.items())


# exercies

# [(name, roll, marks), ...]

data = [
    ("rakibul", 1, 100),
    ("mohammad", 2, 100),
    ("kafka", 3, 75),
    ("bongodev", 5, 99),
]


# print(data[0])
def sortkey(same_name):
    return same_name[2]


print(sorted(data, key=sortkey))
