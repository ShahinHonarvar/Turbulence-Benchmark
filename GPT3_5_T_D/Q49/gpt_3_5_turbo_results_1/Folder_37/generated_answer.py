
def if_decimal_is_divisible(binary_number):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal_number = 0
    for i in range(len(binary_number)):
        decimal_number += int(binary_number[i]) * 2**(len(binary_number)-i-1)
    
    fibonacci_46th = fibonacci(46)
    
    if decimal_number % fibonacci_46th == 0:
        return True
    else:
        return False
