# add = lambda x, y: x + y
# print(add(5, 3))

# lambda is an anonymous function

data = [2, 3, 4, 8, 9]
# print(sorted(data))


# def inc_by_ten(x):
#     return x + 10


# equivalent = lambda x: x + 10
# (name, proximity, goodness)
# key=0

people = [("Shiblu", 1, 4), ("Tamanna", 3, 3), ("Partho", 2, 5)]


def without_lambda_sort(tuple):
    return -1 * tuple[2]


# people.sort(key=lambda ashse: ashse[2])
people.sort(key=without_lambda_sort)
# print(people)
# print(sorted(people, key=))
print(people)
