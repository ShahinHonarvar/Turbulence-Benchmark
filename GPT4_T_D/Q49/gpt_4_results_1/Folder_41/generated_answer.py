
def if_decimal_is_divisible(bin_num):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    dec_num = int(bin_num, 2)
    fib_num = fibonacci(67)

    return dec_num % fib_num == 0
