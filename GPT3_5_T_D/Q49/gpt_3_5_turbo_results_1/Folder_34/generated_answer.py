
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        return fib_seq

    decimal_num = int(binary_string, 2)
    fibonacci_seq = fibonacci(24)

    if decimal_num % fibonacci_seq[23] == 0:
        return True
    else:
        return False
