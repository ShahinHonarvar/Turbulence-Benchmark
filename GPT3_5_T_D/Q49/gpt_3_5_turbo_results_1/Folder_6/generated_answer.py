
def if_decimal_is_divisible(bin_str):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(bin_str, 2)
    fibonacci_185 = fibonacci(185)

    if decimal % fibonacci_185 == 0:
        return True
    else:
        return False
