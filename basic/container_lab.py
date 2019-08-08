# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ['Pinyi', 'River', 'Joseph', 'Idill']
print(students[1])
print(students[-1])

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food"
foods = {'taco', 'pho', 'poke', 'teriyaki'}
for food in foods:
  print(f'{food} goes here is a goood food')


# Exercise 3
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
  'city': 'Chengdu',
  'state': 'Sichuan',
  'population': '123 million'
}

print(f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]} ')

# Exercise 4
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
for key in home_town:
  print(f'{key} = {home_town[key]} ')