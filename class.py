def plus(a, b):
  if type(b) is str:
    return a + len(b)
  else:
    return a + b

print(plus(12, "hello"))

def minus(a, b):
  if type(b) is bool:
    return None
  else:
    return a + b

print(minus(12, False))

def r_plus(a, b):
  if type(b) is int or type(b) is float:
    return a + b
  else:
    return a + len(b)

print(r_plus(10, "python"))