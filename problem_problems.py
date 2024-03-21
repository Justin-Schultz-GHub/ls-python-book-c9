# info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
# info_lst = (info.split(':'))
# print('+'.join(info_lst))


# # Write some code that determines and prints whether the number 3 appears inside each of these lists:
# numbers1 = [1, 3, 5, 7, 9, 11]
# numbers2 = []
# numbers3 = [2, 4, 6, 8]
# numbers4 = ['1', '3', '5']
# numbers5 = ['1', 3.0, '5']

# print(3 in numbers1)
# print(3 in numbers2)
# print(3 in numbers3)
# print(3 in numbers4)
# print(3 in numbers5)


# Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each sequence.
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)


my_tuple_v2 = zip(my_str, my_list, my_tuple, my_range)

print(list(my_tuple_v2))


# # Without running the following code, what values will be printed by line 10?
# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet',
# }

# keys = pets.keys()
# del pets['Dog']
# pets['Snake'] = 'Sssss'
# print(keys)
# # Since dict.keys returns a dictionary view object, any changes made to the
# # dictionary after you call the keys method will be reflected in the list immediately.


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

# Write a comprehension that creates a dict object whose keys are strings and
# whose values are the length of the corresponding key. Only keys with odd lengths
# should be in the dict. Use the set given by my_set as the source of strings.
# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }

# new_dict = {
#     name: len(name)
#     for name in my_set
#     if len(name) % 2 != 0
# }

# print(new_dict)


# # Write a function that computes and returns the factorial of a number by using
# # a for or while loop. The factorial of a positive integer n, signified by n!,
# # is defined as the product of all integers between 1 and n, inclusive:
# # def factorial(num):
# #     result = 1
# #     for number in range(num, 0, -1):
# #         result *= number
        
# #     return result


# def factorial(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1

#     return result
    
# print(factorial(8))


# # The following code uses the randrange function from Python's random library to 
# # obtain and print a random integer within a given range. Using a while loop, it 
# # keeps running until it finds a random number that matches the last number in the
# # range. Refactor the code so it doesn't require two different invocations of randrange.
# import random

# highest = 10

# while True:
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break
    
    
# Write a function called increment_counter that increments a counter variable
# every time it is called. You can test your code with the following:
counter = 0

def increment_counter():
    global counter
    counter += 1
    
        

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101