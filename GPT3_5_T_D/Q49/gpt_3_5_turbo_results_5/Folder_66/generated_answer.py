
def if_decimal_is_divisible(binary):
    def fib(n):
        if n <= 1:
            return n
        else:
            return (fib(n-1) + fib(n-2))

    decimal = int(binary, 2)
    fib120 = fib(120)

    if decimal % fib120 == 0:
        return True
    else:
        return False
