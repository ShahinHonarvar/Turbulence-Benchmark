
def if_decimal_is_divisible(binary_repr):
    def fibonacci(n):
        fib_seq = [0, 1]
        for i in range(2, n+1):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq

    nums = fibonacci(80)
    decimal_num = int(binary_repr, 2)
    return decimal_num % nums[-1] == 0
