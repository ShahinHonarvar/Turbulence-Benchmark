
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

    decimal = int(binary_str, 2)
    fibonacci_126 = fibonacci(126)
    return decimal % fibonacci_126 == 0
