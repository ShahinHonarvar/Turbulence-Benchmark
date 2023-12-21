
def if_decimal_is_divisible(decimal_int):
    def fibonacci(n):
        fib = [0, 1]
        while len(fib) <= n:
            fib.append(fib[-1] + fib[-2])
        return fib

    fib_seq = fibonacci(64)
    decimal_num = int(decimal_int, 2)
    
    return decimal_num % fib_seq[63] == 0
