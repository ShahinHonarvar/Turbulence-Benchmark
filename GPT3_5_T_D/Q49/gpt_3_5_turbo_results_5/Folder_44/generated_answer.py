
def if_decimal_is_divisible(bin_str):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            fib_sequence = [0, 1]
            while len(fib_sequence) <= n:
                next_num = fib_sequence[-1] + fib_sequence[-2]
                fib_sequence.append(next_num)
            return fib_sequence[n]

    decimal = int(bin_str, 2)
    fibonacci_num = fibonacci(159)
    return decimal % fibonacci_num == 0
