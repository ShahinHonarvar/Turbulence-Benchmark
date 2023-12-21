
def if_decimal_is_divisible(bin_rep):
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    num = int(bin_rep, 2)
    fibonacci_number = fib(28)
    if num % fibonacci_number == 0:
        return True
    else:
        return False
