
def if_decimal_is_divisible(bin_str):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

    decimal = int(bin_str, 2)
    fibonacci_99 = fibonacci(99)
    
    return decimal % fibonacci_99 == 0
