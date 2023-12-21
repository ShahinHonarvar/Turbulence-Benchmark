
def if_decimal_is_divisible(decimal_string):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

    decimal_int = int(decimal_string, 2)
    fibonacci_110 = fibonacci(110)

    return decimal_int % fibonacci_110 == 0
