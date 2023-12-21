
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        a,b = 0,1
        for _ in range(n):
            a,b = b, a+b
        return a

    decimal = int(binary, 2)
    fibonacci_189 = fibonacci(188)
    if decimal % fibonacci_189 == 0:
        return True
    else:
        return False
