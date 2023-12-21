
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    number = int(binary, 2)
    fib_125 = fibonacci(125)
    
    if number % fib_125 == 0:
        return True
    else:
        return False
