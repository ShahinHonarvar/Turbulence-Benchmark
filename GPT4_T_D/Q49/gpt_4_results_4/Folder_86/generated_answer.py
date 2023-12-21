
def if_decimal_is_divisible(binary_string):
    def fib(n): 
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
    
    decimal = int(binary_string, 2)
    fib_135th = fib(135)
    
    return decimal % fib_135th == 0
