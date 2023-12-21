
def if_decimal_is_divisible(decimal_string):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return (fibonacci(n-1) + fibonacci(n-2))

    fib_177 = fibonacci(177)
    decimal = int(decimal_string, 2)

    return decimal % fib_177 == 0
