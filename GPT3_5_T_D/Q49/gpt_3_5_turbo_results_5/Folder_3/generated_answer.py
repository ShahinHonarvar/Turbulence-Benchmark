
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)

    fib_35 = fibonacci(35)
    return decimal % fib_35 == 0
