
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n+1):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq

def if_decimal_is_divisible(binary):
    fibonacci_seq = fibonacci(147)
    decimal = int(binary, 2)
    return decimal % fibonacci_seq[147] == 0
