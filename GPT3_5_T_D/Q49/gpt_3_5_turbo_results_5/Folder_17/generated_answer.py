
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        fib_seq = [0, 1]
        while len(fib_seq) <= n:
            next_num = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_num)
        return fib_seq[n]

    decimal = int(binary_str, 2)
    return decimal % fibonacci(154) == 0
