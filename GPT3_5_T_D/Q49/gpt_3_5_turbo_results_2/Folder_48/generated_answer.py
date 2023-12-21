
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib_sequence = [0, 1]
            while len(fib_sequence) <= n:
                fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
            return fib_sequence[n]

    decimal = int(binary, 2)
    fibonacci_number = fibonacci(198)
    return decimal % fibonacci_number == 0
