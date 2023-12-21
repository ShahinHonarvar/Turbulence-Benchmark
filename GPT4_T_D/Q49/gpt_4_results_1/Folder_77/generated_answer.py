
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        else:
            a,b = 0,1
            for _ in range(n-1):
                a,b = b,a+b
            return b

    decimal_number = int(binary_string, 2)
    fib_110 = fibonacci(110)
    
    if decimal_number % fib_110 == 0:
        return True
    else:
        return False
