
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib
    
    decimal = int(binary_string, 2)
    fib_sequence = fibonacci(16)
    return decimal % fib_sequence[15] == 0
