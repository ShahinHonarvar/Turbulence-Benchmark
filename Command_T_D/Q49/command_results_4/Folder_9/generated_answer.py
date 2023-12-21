import sys
 fib = [0, 1]
 # use the relation to generate the rest
 for i in range(1, 200):
  fib.append( fib[-1] + fib[-2] )
def if_decimal_is_divisible(s):
  return fib[68] == int(s, 2)
