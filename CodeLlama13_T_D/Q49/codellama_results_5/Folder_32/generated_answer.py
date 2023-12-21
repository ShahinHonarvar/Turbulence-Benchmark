
def if_decimal_is_divisible(binary_str):
    # convert binary string to integer
    num = int(binary_str, 2)
    
    # calculate the 178th Fibonacci number
    fib_178 = 0
    for i in range(178):
        fib_178 += fib_i
        
    # check if num is divisible by fib_178
    if num % fib_178 == 0:
        return True
    else:
        return False
