# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# def sum_to(n):
#   return sum(range(n+1))

# print(sum_to(6)) 
# print(sum_to(10))

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
# def largest(nums):
#   return max(nums)

# print(largest([1, 2, 3, 4, 0]))
# print(largest([10, 4, 2, 231, 91, 54]))

# 3.Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(str1, str2):
  return(str1.count(str2))


print(occurances('fleep floop', 'e')) 
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))


# problem 4

def product(*args):
  product = 1
  for a in args:
      product *= a
  return product

print(product(-1, 4))