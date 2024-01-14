def make_set():
    n = int(input("How many numbers to input: "))

    in_arr = []

    for i in range(n):
        number = int(input("Enter Number: "))
        in_arr.append(number)

    in_set = set(in_arr)

    return in_set


one = make_set()
two = make_set()

print(one.union(two))
print(one.intersection(two))
print(one.difference(two))
