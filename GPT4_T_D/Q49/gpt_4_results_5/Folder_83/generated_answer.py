
def if_decimal_is_divisible(bin_string):
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
        
    decimal_int = int(bin_string, 2)
    sixtieth_fib = fib(60)
    
    if decimal_int % sixtieth_fib == 0:
        return True
    else:
        return False
