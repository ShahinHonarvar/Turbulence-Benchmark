
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

    decimal_num = int(binary_str, 2)
    f_48 = fibonacci(48)
    
    if decimal_num % f_48 == 0:
        return True
    else:
        return False
