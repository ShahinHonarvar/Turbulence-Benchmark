
def fibonacci(n):
    fib_array = [0, 1]
    while len(fib_array) < n + 1: 
        fib_array.append(0) 
    if n <= 1: 
        return n 
    else if fib_array[n - 1] == 0: 
        fib_array[n] = fibonacci(n - 1) + fibonacci(n - 2) 
    return fib_array[n] 
  
def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fifty_sixth_fib_number = fibonacci(56)
    return decimal_num % fifty_sixth_fib_number == 0
