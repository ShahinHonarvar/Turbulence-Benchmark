
def if_decimal_is_divisible(bin_str):
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    decimal = int(bin_str, 2)
    fibonacci_166 = fib(166)
    
    return decimal % fibonacci_166 == 0
