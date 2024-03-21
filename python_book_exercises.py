# 'True'          # string
# False           # boolean
# (1, 2, 3)       # tuple
# 1.5             # float
# [1, 2, 3]       # list
# 2               # integer
# range(5)        # range
# {1, 2, 3}       # set
# None            # none
# {'foo': 'bar'}  # dictionary



# names = (
#     'asta',
#     'butterscotch',
#     'pudding',
#     'neptune',
#     'darwin',
# )


# pets = {
#     'Asta':         'dog',
#     'Butterscotch': 'cat',
#     'Pudding':      'cat',
#     'Neptune':      'fish',
#     'Darwin':       'lizard',
# }

# print('John' + ' ' + 'Doe')

# number = 4936
# ones = number % 10
# number = number // 10
# tens = number % 10
# number = number // 10
# hundreds = number % 10
# thousands = number // 10

# print(thousands)
# print(hundreds)
# print(tens)
# print(ones)

# int('3.1415') # Raises a ValueError since the string value 3.1415 does not represent a valid integer.

# print('12' < '9') # Evaluates as True since the operands are strings, not numbers.


# # variable & function naming conventions:
# # lowercase only, doesn't start with a digit, ascii only
# index         # idiomatic
# CatName       # non-idiomatic
# lazy_dog      # idiomatic
# quick_Fox     # non-idiomatic
# 1stCharacter  # illegal
# operand2      # idiomatic
# BIG_NUMBER    # non-idiomatic
# π             # non-idiomatic

# # constant naming conventions:
# # no lowercase, doesn't start with a digit, ascii only
# index         # non-idiomatic
# CatName       # non-idiomatic
# snake_case    # non-idiomatic
# LAZY_DOG3     # idiomatic
# 1ST           # illegal
# operand2      # non-idiomatic
# BIG_NUMBER    # non-idiomatic
# Π             # non-idiomatic

# # class naming conventions:
# # starts with capital, no underscores, doesn't start with a digit, ascii only
# index      # non-idiomatic
# CatName    # idiomatic
# Lazy_Dog   # non-idiomatic
# 1ST        # illegal
# operand2   # non-idiomatic
# BigNumber3 # idiomatic
# Πi         # non-idiomatic

# name = 'Victor'
# for i in range(1, 4):
#     if i == 1:
#         print(f'Good morning, {name}.')
#     elif i == 2:
#         print(f'Good afternoon, {name}.')
#     else:
#         print(f'Good evening, {name}.')
        
        
# age = 22
# x = 10

# while x <= 40:
#     if x == 10:
#         print(f'You are {age} years old.')
#         print(f'In {x} years, you will be {x + age}.')
#         x += 10
#     else:
#         print(f'In {x} years, you will be {x + age}.')
#         x += 10


# start_balance = 1000

# for i in range(5):
#     start_balance *= 1.05
# print(start_balance)


# obj = 'ABcd'        # reassignment
# obj.upper()         # neither
# obj = obj.lower()   # reassignment
# print(len(obj))     # neither
# obj = list(obj)     # reassignment
# obj.pop()           # mutation
# obj[2] = 'X'        # mutation
# obj.sort()          # mutation
# set(obj)            # neither
# obj = tuple(obj)    # reassignment


# name = input('What is your name? ')
# last_name = input('And your last name? ')
# print(f'Hello, {name} {last_name}.')


# age = int(input('How old are you? '))
# x = 10

# while x <= 40:
#     if x == 10:
#         print(f'You are {age} years old.')
#         print(f'In {x} years, you will be {x + age}.')
#         x += 10
#     else:
#         print(f'In {x} years, you will be {x + age}.')
#         x += 10


# num1 = int(input('Please enter the first number to be multiplied '))
# num2 = int(input('Please enter the second number to be multiplied '))

# print(f'Your numbers are {num1} and {num2}. Their product is {num1*num2}.')


# def multiply(num1, num2):
#     return num1*num2
    
# def get_number(prompt):
#     entry = input(prompt)
#     return float(entry)


# first_number = get_number('Enter the first number: ')
# second_number = get_number('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}.')


# def multiply():
#     num1 = float(input('Enter the first number to multiply: '))
#     num2 = float(input('Enter the second number to multiply: '))
#     product = num1*num2
#     return f'{num1} * {num2} = {product}'
    
# print(multiply())


# def multiply_numbers(num1, num2, num3):
#     result = num1 * num2 * num3
#     return result

# product = multiply_numbers(2, 3, 4)
# # function name         -- multiply_numbers on lines 171 and 175
# # function arguments    -- 2, 3, 4
# # function definition   -- def multiply_numbers(num1, num2, num3):
# #                       -- result = num1 * num2 * num3
# #                       -- return result

# # function body         -- result = num1 * num2 * num3
# #                       -- return result

# # function parameters   -- num1, num2, num3
# # function invocation   -- multiply_numbers(2, 3, 4)
# # function return value -- 24
# # all identifiers       -- multiply_numbers, num1, num2, num3, result, and product

# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42, 3.141592)
# # 42
# # 3.141592
# # 2


# def get_num(prompt):
#     return float(input(prompt))
    
# def multiply(left, right):
#     return left * right

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')
# # identifiers:
# # multiply, left, right, get_num, prompt, float, input, first_number, second_number, product, print


# def multiply(left, right):
#     return left * right

# def get_num(prompt):
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')
# # identifiers:
# # global    - first_number, second_number, product, multiply, get_num
# # local     - left, right, prompt
# # built-in  - float, input, print


# def multiply(left, right):
#     return left * right

# def get_num(prompt):
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')
# # function names & parameters and their lines:
# # multiply      -- 231, 239
# # left          -- 231, 232
# # right         -- 231, 232
# # get_num       -- 234, 237, 238
# # prompt        -- 234, 235
# # float         -- 235
# # input         -- 235
# # print         -- 240


# def say(message):
#     print(f'==> {message}')

# string1 = input()
# string2 = input()

# say(max(string1.upper(), string2.lower()))
# # function names, method names, and built-in functions
# # functions             -- say
# # methods               -- .upper, .lower
# # built-in functions    -- input, max, print



def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []   

print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))

# # Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False


# def remainders_5(numbers):
#     return [number % 5 for number in numbers]

# numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
# numbers_3 = [0, 5, 10]
# numbers_4 = []


# print(all(remainders_5(numbers_1)))
# print(all(remainders_5(numbers_2)))
# print(all(remainders_5(numbers_3)))
# print(all(remainders_5(numbers_4)))

# #Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True


# False or (True and False)   # False
# True or (1 + 2)             # True
# (1 + 2) or True             # 3
# True and (1 + 2)            # 3
# False and (1 + 2)           # False
# (1 + 2) and True            # True
# (32 * 4) >= 129             # False
# False != (not True)         # False
# True == 4                   # False
# False == (847 == '847')     # True


# def even_or_odd(number):
#     if number % 2 == 0:
#         print(f'{number} is even')
#     else:
#         print(f'{number} is odd')
        
#     print(f'{number} is even' if number % 2 == 0 else f'{number} is odd')
        
        
# even_or_odd(123123123)


# return ('bar' if foo() else qux()) #refactored:
# if foo():
#     return 'bar'
# else:
#     return qux()


# def caps_string(string):
#     print(string.upper() if len(string) > 10 else string)
    
# caps_string('neat')
# caps_string('I really like waffles, although I used to like pancakes more.')


# def number_range(num):
#     if num < 0:
#         print(f'{num} is less than 0.')
#     elif num >= 0 and num <= 50:
#         print(f'{num} is between 0 and 50.')
#     elif num >= 51 and num <= 100:
#         print(f'{num} is between 51 and 100.')
#     else:
#         print(f'{num} is greater than 100.')
    
    
# number_range(0)     # 0 is between 0 and 50
# number_range(25)    # 25 is between 0 and 50
# number_range(50)    # 50 is between 0 and 50
# number_range(75)    # 75 is between 51 and 100
# number_range(100)   # 100 is between 51 and 100
# number_range(101)   # 101 is greater than 100
# number_range(-1)    # -1 is less than 0


# stuff = ('hello', 'world', 'bye', 'now')
# stuff = list(stuff)
# stuff[2] = 'goodbye'
# stuff = tuple(stuff)
# print(stuff)

# # Differences
# Lists are mutable; tuples are immutable.
# List literals use []; tuple literals use ().
# # Similarities
# Lists and tuples are both sequences. Sequences are ordered collections that can use numeric indexes to access the members.
# Lists and tuples are heterogeneous; elements do not need to all be the same type.

# Strings are ordered; you can access the individual characters with indexing.
# Sets are unordered; they don't support indexing.


# print(list(range(3, 17, 4)))


# my_list = [1, 2, 3, [4, 5, 6]]
# another_list = list(my_list)

# print(id(my_list))
# print(id(another_list))
# print(my_list == another_list)
# print(id(my_list[3]))
# print(id(another_list[3]))
# print(my_list[3] == another_list[3])

# The two lists are equal: they are both lists with the same elements.
# The two lists are not the same object: The list constructor creates a new object.
# The two nested lists are equal: they are both lists that have the same elements.
# The two nested lists are the same object: the list constructor creates a shallow copy of the iterable passed as an argument. Shallow copies don't create new nested lists. Instead, only a reference to the nested list gets copied.


# my_dict = {
#     'Alice': 'USA',
#     'Francois': 'Canada',
#     'Inti': 'Peru',
#     'Monika': 'Germany',
#     'Sanyu': 'Uganda',
#     'Yoshitaka': 'Japan,'
# }

# print(my_dict['Alice'])

# my_range = range(0, 25, 3)
# print(my_range[6])

# str1 = 'Launch School'
# print(str1[4:10]) #ch Sch


# tpl_1 = (1, 2, 3, 4, 5)
# tpl_2 = reversed(list(tpl_1)[1:4])
# tpl_2 = tuple(tpl_2)

# print(tpl_2)


# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet',
# }

# print(pets.get('Dog', '<silence>'))


# # Which of the following values can't be used as a key in a dict object, and why?
# 'cat'                           # usable -- strings are immutable and hashable
# (3, 1, 4, 1, 5, 9, 2)           # usable -- tuples are immutable and hashable
# ['a', 'b']                      # unusable -- lists are mutable
# {'a': 1, 'b': 2}                # unusable -- dictionaries are mutable
# range(5)                        # usable -- ranges are immutable and hashable
# {1, 4, 9, 16, 25}               # unusable -- sets are mutable
# 3                               # usable -- integers immutable and hashable
# 0.0                             # usable -- floats immutable and hashable
# frozenset({1, 4, 9, 16, 25})    # usable -- frozen sets are immutable and hashable


# print('abc-def'.isalpha())       # False
# print('abc_def'.isalpha())       # False
# print('abc def'.isalpha())       # False

# print('abc def'.isalpha() and
#       'abc def'.isspace())       # False
      
# print('abc def'.isalpha() or
#       'abc def'.isspace())       # False

# print('abcdef'.isalpha())        # True
# print('31415'.isdigit())         # True
# print('-31415'.isdigit())        # False
# print('31_415'.isdigit())        # False
# print('3.1415'.isdigit())        # False
# print(''.isspace())              # False


# text = "It's probably pining for the fjords!"

# print(text[21:35].rfind('f'))     # 8
# print(text.rfind('f', 21, 35))    # 29


# stuff = [
#     ['hello', 'world'],
#     ['example', 'mem', None, 6, 88],
#     [4, 8, 12],
# ]

# stuff[1][3] = 606

# print(stuff[1])

# cats = {
#     'Pete': {
#         'Cheddar': {
#             'color': 'orange',
#             'enjoys': {
#                 'sleeping',
#                 'snuggling',
#                 'meowing',
#                 'eating',
#                 'birdwatching',
#             },
#         },
#         'Cocoa': {
#             'color': 'black',
#             'enjoys': {
#                 'eating',
#                 'sleeping',
#                 'playing',
#                 'chewing',
#             },
#         },
#     },
# }

# print(cats['Pete']['Cocoa']['enjoys'])


# print('johnson' in 'Joe Johnson')       # False
# print('sen' not in 'Joe Johnson')       # True
# print('Joe J' in 'Joe Johnson')         # True
# print(5 in range(5))                    # False
# print(5 in range(6))                    # True
# print(5 not in range(5, 10))            # False
# print(0 in range(10, 0, -1))            # False
# print(4 in {6, 5, 4, 3, 2, 1})          # True
# print({1, 2, 3} in {1, 2, 3})           # False
# print({3, 2} in {1, frozenset({2, 3})}) # True -- {3, 2} and frozenset({2, 3}) are considered equal sets.


# # Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter (line 130).
# # The updated code should use a for loop to display the future ages.
# age = int(input('How old are you? '))
# print(f'You are {age} years old.')
# for i in range(10, 41, 10):
#         print(f'In {i} years, you will be {age + i} years old.')


# # Use a while loop to print the numbers in my_list, one number per line.
# # Then, do the same with a for loop.
# my_list = [6, 3, 0, 11, 20, 4, 17]

# x = 0
# while x < len(my_list):
#     print(my_list[x])
#     x += 1

# print()

# for i in range(len(my_list)):
#     print(my_list[i])

# print()

# for number in my_list:
#     print(number)


# # Use a while loop to print all numbers in my_list with even values, one number per line.
# # Then, print the odd numbers using a ' for' loop.
# my_list = [6, 3, 0, 11, 20, 4, 17]

# index = 0
# while index < len(my_list):
#     if my_list[index] % 2 == 0:
#         print(my_list[index])
#     index += 1

# print()

# for number in my_list:
#     if number % 2 != 0:
#         print(number)


# # Print all of the even numbers in the following list of nested lists.
# # Don't use any while loops.
# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for lst in my_list:
#     for number in lst:
#         if number % 2 == 0:
#             print(number)


# ------------------------------------------------------------------------------
# # # write code that creates a new list with one element for each number in my_list.
# # # If the original number is an even, then the corresponding element in the new list
# # # should contain the string 'even'; otherwise, the element should contain 'odd'.
# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# new_list = []
# for number in my_list:
#     if number % 2 == 0:
#         new_list.append('even')
#     else:
#         new_list.append('odd')
# print(new_list)

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# result = ['even' if number % 2 == 0 else 'odd'
#           for number in my_list]
# print(result)

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# def odd_or_even(number):
#     return 'even' if number % 2 == 0 else 'odd'

# result = [ odd_or_even(number)
#           for number in my_list ]
# print(result)

# ------------------------------------------------------------------------------

# # Write a find_integers function that returns a list of all the integers from my_tuple:
# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)
            
            
# def find_integers(tple):
#     lst = []
#     for element in tple:
#         if type(element) is int:
#             lst.append(element)
#     return lst # This was how I solved it
#     # return [element
#     #         for element in tple
#     #         if type(element) is int] # This is the better way probably

# integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]


# my_list = [
#   [1, 3, 6, 11],
#   [4, 2, 4],
#   [9, 17, 16, 0],
# ]

# lst = 0
# index = 0
# lst_len = len(my_list)

# while True:
#     if lst == lst_len:
#         break
#     elif index == len(my_list[lst]):
#         lst += 1
#         index = 0
#     elif my_list[lst][index] % 2 == 0:
#         print(my_list[lst][index])
#         index += 1
#     else:
#         index += 1
        

# def sum_of_squares(num1, num2):
#     def square(num):
#         return num*num
#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)


# def all_actions():
#     counter = 0

#     def increment_counter():
#         nonlocal counter
#         counter += 1

#     print(counter)                # 0

#     increment_counter()
#     print(counter)                # 1

#     increment_counter()
#     print(counter)                # 2

#     counter = 100
#     increment_counter()
#     print(counter)                # 101

# all_actions()