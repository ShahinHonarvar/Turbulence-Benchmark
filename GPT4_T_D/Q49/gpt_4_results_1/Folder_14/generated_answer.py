
def if_decimal_is_divisible(binary_string):
    bin_to_decimal = int(binary_string, 2)
    
    def fibonacci(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    if bin_to_decimal % fibonacci(27) == 0:
        return True
    else:
        return False
