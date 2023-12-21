
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary_string, 2)
    return decimal % fibonacci(143) == 0
