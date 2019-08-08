# this is a python comment
my_var = 5
# print('this is my variable', my_var)


#* DATA TYPES
my_representation_of_nothingnes = None

# Booleans
my_true = True
my_false = False

# Numbers
my_integer = 5
my_float = 5.01
my_complex = 2 + 3j

# Operations
my_division = 15 / 5
# print("division:", my_division)

my_integer_division = 15 // 6
# print("int division", my_integer_division)

my_exponent_result = 2 ** 99
# print(my_exponent_result)

# + - * %

#Strings
my_string = 'pickle rick!'
# print(my_string.split(' ')) # ['pickle', 'rick!']
# print(list(my_string)) # ['p', 'i', 'c', 'k', 'l', 'e', ' ', 'r', 'i', 'c', 'k', '!']
# print(my_string.index('r'))
# print('pickle' in my_string)
# print(my_string[3:8])
# print(my_string[::-1])
# print(my_string[::2])


# Logical Operators: ==, !=, or, and, not, 

# Lists
# my_list = [1,2,3]
# print(len(my_list))

# five_zeros = [True] * 5
# print(five_zeros)

# list2 = ['WA', 'OR', 'CA', 'BC', 'Parts of MT and ID']
# last_item = list2[-1]
# print(last_item)

# list2.append('Florida')
# print(list2)
# fl = list2.pop()

one_through_ten = list(range(1,11))
# print(one_through_ten)

a = [1, 23, 12, 99, 82]
a.sort()
a.insert(3, 10000)
print(a)
a.pop(0)
# if 42 in a:
#   # print('yes!')
# elif 99 in a:
#   # print('maybe???')
# else: 
#   print('it is not here')


# dictionary, object
cat ={
  'name': 'Hamlet',
  'age': 7,
  'test': [1,2,3]
}

print(cat['name'])

# type conversion
test = '42'
# print(int(test))
# print(bool(test))
# print(bool())

#! string interpolation
state = 'Washington'
n = 42
year = 1889

my_msg = f"{state} was the {n}th state to join the union in {year}"
print(my_msg)

def number_suffix(n):
  if n in range(11, 13+1):
    return 'th'
  if n % 10 == 1:
    return 'st'
  if n % 10 == 2:
    return 'nd'
  if n % 10 == 3:
    return 'rd'
  
    return 'th'

print(f"{23}{number_suffix(23)}")
#* template = "Hello, I am {} and I like {}"
#* print(template.format('Mike', 'teaching SEI 25'))
# template = "Hello, I am {name} and I like {thing}"
# print(template.format(name = 'Mike', thing ='teaching SEI 25'))

#* Conditional
vip = True
food_place = 'busy'

# if food_place == 'full' and not vip:
#   print('sorry, we have no room')
# elif food_place == 'busy' and not vip:
#   print('Please wait for awhile for a table')
# else: 
#   print('Come on in and have a seat')


#* Loops

# while
n = 0
# while n < 10:
#   print('running the loop ', n)
#   n += 1 # n = n + 1

# print(n)

# for loops
for i in range(0, 9+1):
  print(i)

my_list = ['foo', 'ma', '3', ['hello']]
# for thing in my_list:
#   print(f'this is a {thing}')


foods = ['kale', 'sausage', 'avocado']
print('I like the folloing foods: ')
for i, food in enumerate(foods):
  print(f'{i+1}. {food}')