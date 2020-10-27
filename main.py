def plus(a, b):
  return int(a) + int(b)

def minus(a, b):
  return int(a) - int(b)

def times(a, b):
  return int(a) * int(b)

def division(a, b):
  return int(a) / int(b)

def negation(a, b):
  return -int(a), -int(b)

def power(a, b):
  return int(a) ** int(b)

def reminder(a, b):
  return int(a) % int(b)

r_plus = plus(3, 2)
r_minus = minus(4, 2)
r_times = times(3, 2)
r_division = division(6, 2)
r_negation = negation(5, 2)
r_power = power(7, 2)
r_reminder = reminder(5, 2)

print(r_plus)
print(r_minus)
print(r_times)
print(r_division)
print(r_negation)
print(r_power)
print(r_reminder)
