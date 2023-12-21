
def if_decimal_is_divisible(binary_string):
    def nth_fib(n):
        a,b = 0,1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal = int(binary_string, 2)
    return decimal % nth_fib(80) == 0
