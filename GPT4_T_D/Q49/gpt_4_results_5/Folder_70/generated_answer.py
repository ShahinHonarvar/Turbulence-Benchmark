
def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)

    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    return decimal % fib(137) == 0
