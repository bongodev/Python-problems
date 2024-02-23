numbers = [1, 2, 3, 4, 5]


def do_square(x):
    return x * x


def do_square_print(x):
    x = x + 5
    print("got ", x)


squared = list(map(do_square_print, numbers))
# squared = list(map(lambda x: x * x, numbers))
# squared = map(lambda x: x * x, numbers)

print(squared)


# def function_er_vitore_function(input_function):
#     # print(input_function(5))
#     print("hello")


# function_er_vitore_function(do_square)
# print(do_square)
# map applies to iterables
# list, tuples

# tup = ("sajon", "bongodev", 5)

# tup[1]

# exercise
# convert lowercase string to uppercase

words = ["hello", "world", "python"]

# output: ["HELLO", "WORLD", "PYTHON"]  # with map and lambda
