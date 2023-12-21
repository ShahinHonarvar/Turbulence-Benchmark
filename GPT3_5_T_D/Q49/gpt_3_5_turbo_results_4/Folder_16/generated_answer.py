
def if_decimal_is_divisible(dec):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n+1):
                fib.append(fib[i-1] + fib[i-2])
            return fib[n]

    decimal = int(dec, 2)
    fibonacci_128 = fibonacci(128)
    return decimal % fibonacci_128 == 0
