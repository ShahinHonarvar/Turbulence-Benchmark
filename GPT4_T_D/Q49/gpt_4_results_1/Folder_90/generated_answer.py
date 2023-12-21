
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

    decimal = int(binary_representation, 2)
    fibonacci_177 = fibonacci(177)
    return decimal % fibonacci_177 == 0
