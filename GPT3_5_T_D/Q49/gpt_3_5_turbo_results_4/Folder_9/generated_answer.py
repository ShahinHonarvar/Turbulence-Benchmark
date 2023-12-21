
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n < 2:
            return n
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]
    
    decimal = int(binary, 2)
    fib_68 = fibonacci(68)
    
    return decimal % fib_68 == 0
