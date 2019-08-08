import math

def tempConvert(tempInF):
  tempInC = (tempInF - 32) * 5 / 9
  tempInK = tempInC + 273.15
  print(f"Current temperature is {tempInF}F ({tempInC}C, {tempInK}K)")

tempConvert(83)

def sayHello():
  name = input('Your Name: ')
  age = input('How old are you?: ')
  result = 'Hello, ' + name + '. You are ' + age + ' years old.'
  print(result)

# sayHello()

def countNameLength():
  name = input('May I have your full name please?: ')
  length = len(name) - name.count(' ')
  print(f"Hi, {name}, your name is {length} characters long.")

# countNameLength()

def getSphereV():
  radius = input('What is the radius of your sphere?: ')
  result = math.pi * int(radius)**3 * 4 /3
  print(f'The volume of your sphere is {result}')

# getSphereV()

