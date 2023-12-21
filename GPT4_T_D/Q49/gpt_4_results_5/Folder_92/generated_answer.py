
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n<=1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    decimal_representation = int(binary_string, 2)
    if decimal_representation % fibonacci(7) == 0:
        return True
    else:
        return False
