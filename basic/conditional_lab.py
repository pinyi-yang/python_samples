def checkEven(n):
  if n%2:
    print(f'{n} is odd.')
  else:
    print(f'{n} is even')

checkEven(2)
checkEven(3)

def lessThan140(string):
  if (len(string) < 140):
    print(string)
  else:
    print(f'error: the length of string is {len(string)}, greater than 140.')

lessThan140('cd /Users/Pinyi/code/unit4/python/basic ; env PYTHONIOENCODING=UTF-8 PYTHONUNBUFFERED=1 /usr/local/opt/python/bin/python3.7 /Users/Pinyi/.vscode/extensions/ms-python.python-2019.8.29288/pythonFiles/ptvsd_launcher.py --default --client --host localhost --port 49595 /Users/Pinyi/code/unit4/python/basic/conditional_lab.py ')
lessThan140('test')

def getGrade(score):
  gradeBySore = ['A', 'B', 'C', 'D', 'F']
  gradeIndex = (100-score) // 10
  if gradeIndex > 4:
    print("Your grade is F")
  else:
    print(f'Your grade is {gradeBySore[gradeIndex]}')

getGrade(94)
getGrade(60)
getGrade(75)
getGrade(40)


def printPosition(letter, num):
  decode = {
    "1": "upper",
    '2': 'lower',
    'A': 'left',
    'B': 'right'
  }

  print(f'{decode[str(num)]} {decode[letter]}')

printPosition('A', 1)
printPosition('B', 2)