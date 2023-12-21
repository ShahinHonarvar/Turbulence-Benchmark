
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            while len(fib) <= n:
                fib.append(fib[-1] + fib[-2])
            return fib[n]

    decimal = int(binary, 2)
    fibonacci_28 = fibonacci(28)
    return decimal % fibonacci_28 == 0
