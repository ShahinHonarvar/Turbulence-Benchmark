
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[n-1]

    decimal_integer = int(binary_string, 2)
    fibonacci_number = fibonacci(198)

    return decimal_integer % fibonacci_number == 0
