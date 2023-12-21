
def if_decimal_is_divisible(binary_string):
    def fib(n):
        if n <= 1:
            return n
        else:
            a, b = 0, 1
            for i in range(2, n+1):
                a, b = b, a+b
            return b

    num = int(binary_string, 2)
    fib_num = fib(196)

    if num % fib_num == 0:
        return True
    else:
        return False
