def sum(m, n):
  if n < 0:
    n = -n
    for i in range(0, n):
      m -= 1
  else:
    for i in range(0, n):
      m += 1
  return m

def divide(m, n):
  result = 0
  coeff = 1
  if m < 0:
    m = -m
    coeff = -1
  
  if n < 0:
    n = -n
    coeff = -coeff

  while m > 0:
    result += 1
    m -= n
  return result * coeff

print(sum(-4,-2))
print(divide(-4, -2))
print(divide(-4, 2))
print(divide(4, -2))
print(divide(4, 2))