
def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n+1:
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    return fib[n]

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_76 = fibonacci(76)
    return decimal % fib_76 == 0
