def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  return False

def sum_double(a, b):
  if a != b:
    return a+b
  return 2*(a+b)

def sleep_in(weekday, vacation):
  if not weekday or weekday and vacation:
    return True
  return False

def set_square(x):
  global ret_square
  ret_square = x**2