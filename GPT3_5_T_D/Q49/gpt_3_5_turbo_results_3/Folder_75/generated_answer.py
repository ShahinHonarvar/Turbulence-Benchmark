
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence[n]

    decimal_num = int(binary_str, 2)
    fibonacci_num = fibonacci(189)
    return decimal_num % fibonacci_num == 0
