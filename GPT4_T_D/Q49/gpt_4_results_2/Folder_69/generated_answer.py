
def fib(num): 
  fib_sequence = [0, 1]
  
  while(len(fib_sequence) < num):
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

  return fib_sequence[-1]

def if_decimal_is_divisible(bin_string): 
  decimal = int(bin_string, 2)
  nth_fibonacci = fib(171)
  
  if decimal % nth_fibonacci == 0: 
    return True
  else:
    return False
