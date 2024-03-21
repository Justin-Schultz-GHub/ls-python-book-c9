# car = {
#     'type': 'sedan',
#     'color': 'blue',
#     'mileage': 80_000,
# }

# car['year'] = 2003
# del car['mileage']


# print(car)                  # {'type': 'sedan', 'color': 'blue', 'year': 2003}
# print(car['type'])          # sedan
# print(car['color'])         # blue
# print(car['year'])          # 2003
# print(car.get('mileage'))   # None
# print(len(car))             # 3


# student = {
#     'id': 123,
#     'grade': 'B',
# }

# print('name' in student)      # False
# print('grade' in student)     # True

# vehicles = {
#     'car': {
#         'type': 'sedan',
#         'color': 'blue',
#         'year': 2003,
        
#     },
#     'truck': {
#         'type': 'pickup',
#         'color': 'red',
#         'year': 1998,
#     },
# }

# print(vehicles['car'])          #{'type': 'sedan', 'color': 'blue', 'year': 2003}
# print(vehicles['car']['year'])  #2003

# # list instead of dictionary
# car = [
#     ['type', 'sedan'],
#     ['color', 'blue'],
#     ['year', 2003],
# ]

# print(car[1][1]) #blue


# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    10,
# }

# half_numbers = []
# for value in numbers.values():
#     half_numbers.append(value // 2)

# print(half_numbers)

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    10,
# }

# for key, value in numbers.items():
#     print(f'A {key} numbers is {value}.')