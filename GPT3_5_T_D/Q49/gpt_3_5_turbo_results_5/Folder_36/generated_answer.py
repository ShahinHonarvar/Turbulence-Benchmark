
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))

    fib_150 = fibonacci(150)
    if decimal % fib_150 == 0:
        return True
    else:
        return False
