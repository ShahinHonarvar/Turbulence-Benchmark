
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    decimal_integer = int(binary_string, 2) 
    if decimal_integer % fibonacci(90) == 0: 
        return True
    else:
        return False
