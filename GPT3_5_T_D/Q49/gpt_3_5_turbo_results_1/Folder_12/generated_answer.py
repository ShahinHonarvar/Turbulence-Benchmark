
def if_decimal_is_divisible(decimal):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]
    
    fib_66 = fibonacci(66)
    decimal_int = int(decimal, 2)
    
    if decimal_int % fib_66 == 0:
        return True
    else:
        return False
