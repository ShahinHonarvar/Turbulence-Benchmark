
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib

    fibonacci_sequence = fibonacci(54)
    decimal_integer = int(binary_string, 2)

    if decimal_integer % fibonacci_sequence[53] == 0:
        return True
    else:
        return False
