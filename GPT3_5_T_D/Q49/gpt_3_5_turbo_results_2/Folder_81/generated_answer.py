
def if_decimal_is_divisible(binary):
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    decimal = int(binary, 2)
    fib_97 = fib(97)
    return decimal % fib_97 == 0
