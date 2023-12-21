
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[n-1]

    dec_int = int(binary_str, 2)
    fib_137 = fibonacci(137)
    
    return dec_int % fib_137 == 0
