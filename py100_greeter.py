# def greet(langcode):
#     if langcode == 'en':
#         return 'Hi!'
#     elif langcode == 'fr':
#         return 'Salut!'
#     elif langcode == 'pt':
#         return 'Ola!'
#     elif langcode == 'de':
#         return 'Hallo!'
#     elif langcode == 'sv':
#         return 'Hej!'
#     else:
#         return 'Haai!'
    


# def extract_language(locale):
#     return locale.split('_')[0]


# def extract_region(locale):
#     return locale.split('_')[1].split('.')[0]


# def local_greet(locale):
#     language = extract_language(locale)
#     region = extract_region(locale)
    
#     if language == 'en' and region == 'US':
#         return 'Hey!'
#     elif language == 'en' and region == 'GB':
#         return 'Hello!'
#     elif language == 'en' and region == 'AU':
#         return 'Howdy!'
#     else:
#         return greet(language)



# print(local_greet('en_US.UTF-8'))       # Hey!
# print(local_greet('en_GB.UTF-8'))       # Hello!
# print(local_greet('en_AU.UTF-8'))       # Howdy!

# print(local_greet('fr_FR.UTF-8'))       # Salut!
# print(local_greet('de_CA.UTF-8'))       # Hallo!
# print(local_greet('sv_MA.UTF-8'))       # Hej!



def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('de_CA.UTF-8'))       # Hallo!
print(local_greet('sv_MA.UTF-8'))       # Hej!


# def greet(langcode):
#     if langcode == 'en':
#         return ''


# def extract_language(locale):
#     return locale[0:2]

# def extract_region(locale):
#     return locale.split('_')[1].split('.')[0]



# def local_greet(locale):
#     language = extract_language(locale)
#     region = extract_region(locale)
    
#     if language == 'en' and region == 'US':
#         return 'Hey!'
#     elif language == 'en' and region == 'GB':
#         return 'Hello!'
#     elif language == 'en' and region == 'AU':
#         return 'Howdy!'
#     else:
#         return greet(language)











# print(greet('en'))         # Hi!
# print(greet('fr'))         # Salut!
# print(greet('pt'))         # Olá!
# print(greet('de'))         # Hallo!
# print(greet('sv'))         # Hej!
# print(greet('af'))         # Haai!


# print(extract_language('en_US.UTF-8'))      # en
# print(extract_language('en_GB.UTF-8'))      # en
# print(extract_language('ko_KR.UTF-16'))     # ko


# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR


