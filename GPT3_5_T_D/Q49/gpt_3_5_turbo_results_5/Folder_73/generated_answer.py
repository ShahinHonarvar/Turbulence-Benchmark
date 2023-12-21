
def if_decimal_is_divisible(binary_repr):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary_repr, 2)
    fib_164 = fibonacci(164)

    if decimal % fib_164 == 0:
        return True
    else:
        return False
