from cs50 import get_int, get_float, get_string
x = get_float("x: ")
y = get_float("y: ")
#print('X is divisible by Y' if x % y == 0 else  'X is not divisible by Y')
print("dont divisible by 0" if y == 0  else 'X is divisible by Y' if x % y == 0 else  'X is not divisible by Y')
