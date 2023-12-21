
def if_decimal_is_divisible(binary_string):
    def get_fibonacci(n):
        fib = [0, 1]
        while len(fib) <= n:
            fib.append(fib[-1] + fib[-2])
        return fib[n]

    decimal = int(binary_string, 2)
    fibonacci_190 = get_fibonacci(190)
    
    return decimal % fibonacci_190 == 0
