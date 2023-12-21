
def if_decimal_is_divisible(decimal_string):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    fib = fibonacci(125)

    decimal = int(decimal_string, 2)

    return decimal % fib[125] == 0
