# a = int(input('Enter a number:'))
# b = int(input('Enter another number:'))

# try-except block | try-catch block

# try:
#     result = 10/0
# except (ZeroDivisionError, TypeError) as e:
#     print('error occurred!')

#     # log or record the error
#     print('Details: ', e)
# else:
#     print('addition successful')
#     # print(result)
# finally:
#     print('code finished finally!')

# result = 10 + 'five'


# raise your own exceptions
# def check_age(age):
#     if type(age) == str:
#         raise TypeError('age cannot be a string')
#     if age < 0:
#         raise ValueError('Age cannot be negative!')
#     return 'Welcome to the club!'

# age_input = int(input('Enter your age:'))

# try:
#     message = check_age(age_input)
# except (ValueError, TypeError) as e:
#     print('Error: ', e)
# else:
#     print(message)

# checking variable types in python
# print(type('hello'))
# str_in = 'hello'
# num_in = 5.0

# if type(num_in) == int:
#     print('is int')
# else:
#     print('not int')


# # custom exceptions

# try:
#     raise TypeError('amar iccha')
# except:
#     print('vul hoise')
# else:
#     print('iccha nai')
# finally:
#     print('iccha sesh')

# # catch all exceptions and know what the are

# try:
#     raise TypeError('amar iccha')
# except Exception as error:
#     print('error details: ', error)


# best practices: being specific
try:
    # another_result = 10/0
    result = "five" + "five"
    # more code
except TypeError:
    print("wrong types")
except ZeroDivisionError:
    print("divided by zero")
except ValueError:
    print("wrong values")
except Exception:
    print("other error")
else:
    print("calculation thikthak")
    print("result: ", result)
finally:
    print("code completed")
