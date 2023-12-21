
def if_decimal_is_divisible(decimal_binary):
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        fib_prev_1 = 0
        fib_prev_2 = 1

        for i in range(2, n + 1):
            fib_current = fib_prev_1 + fib_prev_2
            fib_prev_1, fib_prev_2 = fib_prev_2, fib_current

        return fib_current

    decimal = int(decimal_binary, 2)
    fib_number = fibonacci(38)

    return decimal % fib_number == 0
