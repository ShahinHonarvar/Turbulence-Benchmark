
def if_decimal_is_divisible(binary_string):
    def Fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

    decimal_integer = int(binary_string, 2)
    fibonacci_178 = Fibonacci(178)
    return decimal_integer % fibonacci_178 == 0
