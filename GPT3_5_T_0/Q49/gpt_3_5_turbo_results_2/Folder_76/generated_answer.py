
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary, 2)
    fibonacci_188 = fibonacci(188)

    if decimal % fibonacci_188 == 0:
        return True
    else:
        return False
