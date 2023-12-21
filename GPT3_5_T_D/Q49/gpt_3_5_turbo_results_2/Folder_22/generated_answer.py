
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
            
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, (a + b)
        
        return b
    
    decimal = int(binary, 2)
    twentieth_fib = fibonacci(20)
    
    return decimal % twentieth_fib == 0
