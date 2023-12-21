
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n+1):
                fib.append(fib[i-1] + fib[i-2])
            return fib[n]

    decimal_integer = int(binary_representation, 2)
    fib_110 = fibonacci(110)
    return decimal_integer % fib_110 == 0
