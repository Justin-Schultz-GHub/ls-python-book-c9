# print(len('These aren\'t the droids you\'re looking for.'))

# confetti = 'confetti floating everywhere'
# confetti_upper = confetti.upper()
# print(confetti_upper)

# string1 = 'RoGeR'
# string2 = 'Roger'
# string3 = 'DAVE'

# print(string1.casefold() == string2.casefold())
# print(string1.casefold() == string3.casefold())


# string = '''A pirate I was meant to be!
# Trim the sails and roam the sea!
# A pirate I was meant to be!
# Trim the sails and roam the sea!'''
        
# print(string)

# char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

# print('x' in char_sequence)

# def is_empty(string):
#     return not string
    

# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True


# def is_empty_or_blank(string):
#     # return len(string.strip(' '))
#     # return string.strip() == ''
#     return not string.strip(' ')

# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True

# def caps_string(word):
#     return word.title()


# def caps_string(string):
#     words = string.split(' ')
#     word_list = []
    
#     for word in words:
#         word_list.append(word.capitalize())
#     return ' '.join(word_list)
    


# string = 'launch school tech & talk'
# result = caps_string(string)
# print(result)  # Launch School Tech & Talk


# def starts_with(word, prefix):
#     # return word.startswith(prefix)
#     prefix_length = len(prefix)
#     return word[0:prefix_length] == prefix

# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True


# def count_substrings(string, substring):
#     return string.count(substring)


# print(count_substrings("lemon lemon lemon", "lemon")) # 3
# print(count_substrings("laLAlaLA", "la")) # 2
# print(count_substrings("launch", "uno")) # 0