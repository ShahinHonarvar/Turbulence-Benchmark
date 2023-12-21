
def if_decimal_is_divisible(binary_string):
    binary_integer = int(binary_string, 2)

    def fibonacci(n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n-1):
                a, b = b, a+b
            return b

    fibo_48 = fibonacci(48)
    if binary_integer % fibo_48 == 0:
        return True
    else:
        return False
