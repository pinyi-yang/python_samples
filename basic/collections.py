import datetime
student = {
  'name': "Anthony",
  'course': "SEI",
  'week_number': 10.5
}

today = datetime.date.today()
print(today.year, today.month, today.day, datetime.date(today.year, today.month, today.day).weekday())


colors = ['red', 'blue', 'green']
colors[-1] = 'marooooon'

colors.append('blue')
colors.extend(['green', 'yellow', 'purple'])


colors.insert(1, 'pink')
# print(colors)
colors.pop(4)
del colors[-2]
# print(colors)


COLORS = ('red', 'purple', 'blue', 'green')
print(len(COLORS))

print(COLORS.index('blue'))

for index, color in enumerate(COLORS):
  print(index+1, ':', color)

print(COLORS[2:4])