# def first(word_list):
#     if word_list:
#         return word_list[0]
#     else:
#         return None
    
    
# print(first([]))  # Earth


# def last(words):
#     if words:
#         return words[-1]
#     else:
#         return None

# print(last(['Earth', 'Moon', 'Mars']))  # Mars
# print(last([]))  # None



# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# energy.remove('fossil')
# energy.append('geothermal')


# print(energy)


# ------------------------------------

# def alphabet_list():
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'    
#     letters = []
#     i = 0
    
#     for letter in alphabet:
#         letters.append(alphabet[0 + i])
#         i += 1
#     return letters
    
# print(alphabet_list())

# alphabet = 'abcdefghijklmnopqrstuvwxyz'  
# print(list(alphabet))

# alphabet = 'abcdefghijklmnopqrstuvwxyz'    
# letters = []
# i = 0

# for letter in alphabet:
#     letters.append(alphabet[0 + i])
#     i += 1

# print(letters)

# -------------------------------------

# def over_one_hundred():
#     scores = [96, 47, 113, 89, 100, 102]    
#     count = 0
    
#     for score in scores:
#         if score >= 100:
#             count += 1
#     return count
    
# print(over_one_hundred())

# scores = [96, 47, 113, 89, 100, 102]
# count = [score for score in scores if score >= 100]
# print(len(count))


# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# for groups in vocabulary:
#     for word in groups:
#         print(word)


# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'

# # print(type(some_value1), type(some_value2))

# print(isinstance(some_value1, list))  # True
# print(isinstance(some_value2, list))  # False

# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']
                
# def contains(destination, lst):
#     for place in lst:
#         if place == destination:
#             return True
        
#     return False
            
# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False

# # def contains(element, lst):
# #     index = 0
# #     while index < len(lst):
# #         if lst[index] == element:
# #             return True

# #         index += 1

# #     return False


# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
# joined_passcode = ''

# for i in range(len(passcode)):
#     if i > 0:
#         joined_passcode += '-'

#     joined_passcode += passcode[i]

# print(joined_passcode)  # 11-jZ5-hQ3f*-8!7g3-p3Fs



# grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
#                 'carrots', 'broccoli', 'hummus']

# while grocery_list:
#     checked_item = grocery_list.pop(0)
#     print(checked_item)
    
# print(grocery_list)