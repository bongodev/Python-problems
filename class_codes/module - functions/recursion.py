# concepts
# base case
# recursive case


# recursive function

# a function that calls itself


# recursive case
def function():
    print("hello")
    function()


# base case - returns from the function


# recursive function skeleton
# def recur_skel(a):
#     # base case
#     if a < 0:
#         return

#     # function
#     print("got ", a)

#     # call the function itself
#     recur_skel(a - 5)


# recur_skel(88)

# factorial calculate
# notes: 0! = 1
# 5! = 5 * 4 * 3 * 2 * 1
# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1


# def factorial(n):
#     # base case
#     if n == 0:
#         return 1

#     # recursion
#     return n * factorial(n - 1)


# result = factorial(5)

# print(result)  # 120

# -> factorial(5): 5 * factorial(4) : 5 * 24 = 120
# -> factorial(4): 4 * factorial(3) : 4 * 6 = 24
# -> factorial(3): 3 * factorial(2) : 3 * 2 = 6
# -> factorial(2): 2 * factorial(1) : 2 * 1 = 2
# -> factorial(1): 1 * factorial(0) : 1 * 1 = 1
# -> factorial(0): 1


# sum of natural numbers
# n = 1 + 2 + 3 + ... + n


# def sum(n):
#     # base case
#     if n == 0:
#         return 0

#     # recursion
#     return n + sum(n - 1)


# print(sum(5))  # 15

# exercise

# first one
# reverse a string w/ recursion
# reverse_recur(hello) -> olleh

# second one
# fibonacci using recursion
# 0, 1, 1, 2, 3, 5, 8, ....

# find if a string is palindrome
# palindrome strings: radar | python
# is_palindrome(radar): True, is_palindrome(python): False

# slicing
# data = "hello"
# # 1-th to before last substring
# sub = data[1:-1]
# print(sub)


# radar
def is_palindrome(input):
    # base case
    if len(input) <= 1:
        return True

    # check if first and last characters are the same
    if input[0] == input[-1]:
        return is_palindrome(input[1:-1])

    return False


#


# def reverse_recur_inplace(input):
#     # base case
#     if len(input) <= 1:


#     # swap first and last characters
#     input[0], input[-1] = input[-1], input[0]
#     return reverse_recur_inplace(input[1:-1])


# # swap syntax in python
# y, x = x, y


# print(is_palindrome("python"))
# function(n) -> function(n-1) + function(n-2)
