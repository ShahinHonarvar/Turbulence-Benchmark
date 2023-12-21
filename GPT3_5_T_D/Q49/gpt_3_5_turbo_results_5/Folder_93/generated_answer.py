
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib
    
    fibonacci_seq = fibonacci(59)
    decimal = int(binary, 2)
    return decimal % fibonacci_seq[58] == 0
