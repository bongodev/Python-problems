# Recursively Find Max: Write a recursive function to find the maximum number in a list.
# [a, b, c, d, e]
# [b, c, d, e]
# [b, d, e]
# [d, e]
# [e]


def findMax(input_arr):
    print("got input: ", input_arr)
    # base case
    if len(input_arr) < 2:
        return input_arr[0]

    # recursive case
    a = input_arr[0]
    b = input_arr[1]

    # bigger = a
    # if a < b:
    #     bigger = b
    bigger = a if a > b else b

    sliced_arr = input_arr[2:]
    print("sliced:", sliced_arr)
    sliced_arr.append(bigger)
    print("after append", sliced_arr)

    return findMax(sliced_arr)


result = findMax([5, 6, 3, 11])
print("result: ", result)
