
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n + 1):
                fib.append(fib[i-1] + fib[i-2])
            return fib[n]

    decimal = int(binary, 2)
    fibonacci_108 = fibonacci(108)

    if decimal % fibonacci_108 == 0:
        return True
    else:
        return False
