
def if_decimal_is_divisible(binary_num):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal_num = int(binary_num, 2)
    fibonacci_199 = fibonacci(199)
    
    return decimal_num % fibonacci_199 == 0
