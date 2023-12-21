
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal_integer = 0
    for i in range(len(binary_string)):
        decimal_integer += int(binary_string[i]) * 2**(len(binary_string)-1-i)

    fibonacci_170 = fibonacci(170)
    
    if decimal_integer % fibonacci_170 == 0:
        return True
    else:
        return False
