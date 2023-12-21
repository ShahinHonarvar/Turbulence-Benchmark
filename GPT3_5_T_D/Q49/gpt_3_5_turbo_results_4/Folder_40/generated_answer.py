
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    
    decimal_integer = int(binary_string, 2)
    fourth_fibonacci_number = fibonacci(4)
    
    if decimal_integer % fourth_fibonacci_number == 0:
        return True
    else:
        return False
