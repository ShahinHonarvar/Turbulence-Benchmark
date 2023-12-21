
def if_decimal_is_divisible(binary_string):
    def fib(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a+b
        return b
    decimal = int(binary_string, 2)
    return decimal % fib(17) == 0
