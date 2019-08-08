# Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n.
def sum_to(n):
  sum = 0
  for i in range(n+1):
    sum += i
  return sum

# print(sum_to(5))

# Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers. 
def largest(l):
  max = l[0]
  for num in l:
    if(num > max):
      max = num
  return max

# print(largest([10, 4, 2, 231, 91, 54]))

# Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:
def occurrances(string, chars):
  occur = 0
  length = len(chars)
  for i in range(len(string)):
    if(string[i: i+length] == chars):
      occur += 1
  return occur

# print(occurrances('fleep floop', 'ee'))

# Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product
def product(*args):
  result = 1
  for arg in args:
    result *= arg
  return result

# print(product(1,5,3,5,2))


#Primes, get all primes for a number
def getPrimes(n, primes = []):
  for i in range(2, (n//2)+1):
    if (n % i == 0):
      if (i not in primes):
        primes.append(i)
      return getPrimes(n//i, primes)
  return primes

print(getPrimes(64))
      
