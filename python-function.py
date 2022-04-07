# 1)
def sum_to(n):
  sum = 0
  count = 1
  while count <= n:
    sum += count
    count += 1
  return sum

print(sum_to(10))

# 2)
def largest(numList):
  max = sorted(numList)
  return max[-1]

print(largest([100, 2, 9, 4, 0]))

# 3)
def occurrences(input, segment):
  count = input.count(segment)
  return count

print(occurrences('fleep floop', 'ee'))

# 4)
def product(*args):
  x = 1
  for arg in args:
    x *= arg
  return x

print(product(4, 0.5, 5))
