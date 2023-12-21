
def if_decimal_is_divisible(binary_repr):
    def fib(n):
        if n <= 1:
            return n
        else:
            a, b = 0, 1
            for _ in range(2, n+1):
                a, b = b, a+b
            return b
    num = int(binary_repr, 2)
    if num % fib(28) == 0:
        return True
    else:
        return False
