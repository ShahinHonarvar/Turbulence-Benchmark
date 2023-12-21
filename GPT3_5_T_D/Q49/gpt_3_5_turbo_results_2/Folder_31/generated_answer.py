
def if_decimal_is_divisible(decimal_binary):
    def fibonacci(n):
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence[n]

    decimal = int(decimal_binary, 2)
    fibonacci_69 = fibonacci(69)

    return decimal % fibonacci_69 == 0
