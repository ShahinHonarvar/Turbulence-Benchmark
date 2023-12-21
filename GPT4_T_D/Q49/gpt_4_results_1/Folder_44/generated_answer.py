
from sympy import fib

def if_decimal_is_divisible(binary_decimal):
    decimal_equal = int(binary_decimal, 2)
    fibonacci_number = fib(159)
    
    if decimal_equal % fibonacci_number == 0:
        return True
    else:
        return False
