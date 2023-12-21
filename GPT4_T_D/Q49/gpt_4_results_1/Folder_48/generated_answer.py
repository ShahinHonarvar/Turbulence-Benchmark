
def if_decimal_is_divisible(bin_str):
  num = int(bin_str, 2)
  fib_list = [0, 1]
  
  for i in range(2, 198):
    fib_list.append(fib_list[-1] + fib_list[-2])

  return num % fib_list[-1] == 0
