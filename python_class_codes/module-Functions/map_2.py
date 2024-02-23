# maps

# map(function, iterable)
# input_list = [1, 2, 3, 4, 5]

# def function_to_apply(x):
#     return x * x

# output_list = map(function_to_apply, input_list)

# print(list(output_list))

# c -> (c * 9/5) + 32

temperature_c = [0, 25, 30, 35]


def convert_c2f(c):
    return (c * 9 / 5) + 32


# temperature_f = map(convert_c2f, temperature_c)

temperature_f = []

for temp in temperature_c:
    temp_f = convert_c2f(temp)
    temperature_f.append(temp_f)

print(temperature_f)
