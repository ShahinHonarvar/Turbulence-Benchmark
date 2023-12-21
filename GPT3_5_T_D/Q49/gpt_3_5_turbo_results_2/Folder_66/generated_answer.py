
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            a, b = 0, 1
            for _ in range(n-1):
                a, b = b, a + b
            return b

    decimal = int(binary, 2)
    fib_120 = fibonacci(120)

    if decimal % fib_120 == 0:
        return True
    else:
        return False
