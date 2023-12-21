
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal_num = int(binary_string, 2)
    fib_number = fibonacci(119)
    
    if decimal_num % fib_number == 0:
        return True
    else:
        return False
