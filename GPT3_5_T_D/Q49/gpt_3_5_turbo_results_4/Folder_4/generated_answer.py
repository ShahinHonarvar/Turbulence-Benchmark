
def if_decimal_is_divisible(binary_num):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        
    decimal_num = int(binary_num, 2)
    fib_118 = fibonacci(117)
    
    return decimal_num % fib_118 == 0
