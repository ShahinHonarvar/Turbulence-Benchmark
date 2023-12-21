
def if_decimal_is_divisible(binary):
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

    decimal = int(binary, 2)
    fib_84 = fibonacci(84)
    return decimal % fib_84 == 0
