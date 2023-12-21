
def if_decimal_is_divisible(decimal):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for i in range(2, n + 1):
                a, b = b, a + b
            return b
    
    return int(decimal, 2) % fibonacci(139) == 0
