
def if_decimal_is_divisible(bin_str):
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
    
    decimal = int(bin_str, 2)
    fibonacci_number = fibonacci(139)
    
    if decimal % fibonacci_number == 0:
        return True
    else:
        return False
