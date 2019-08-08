class Car():
  def __init__(self, name='', color = 'white', wheel = 4, door = 4):
    self.name = name
    self.color = color
    self.wheel = wheel
    self.door = door

  def drive(self, miles = 0):
    print(f'Your {self.door} doors, {self.color} {self.name} drives forward {self.miles} miles.')



class Dog():
  total_dogs = 0 # will have same value in same globe scope (node and react have different globe scope)
  def __init__(self, name='', age=0):
    self.name = name
    self.age = age
    Dog.total_dogs += 1
  
  def bark_hello(self):
    print(f'Woof! I am called {self.name} and I am {self.age} human-years old.')
    print(f'There are {Dog.total_dogs} dogs in this room.')

gracie = Dog('Gracie', 8)
gracie.bark_hello()

spitz = Dog('Spitz', 5)
spitz.bark_hello()

buck = Dog('Buck', 3)
buck.bark_hello()