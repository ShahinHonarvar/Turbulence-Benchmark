
def if_decimal_is_divisible(bin_string):
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    num = int(bin_string, 2)
    fib_num = fib(164)
    return num % fib_num == 0
