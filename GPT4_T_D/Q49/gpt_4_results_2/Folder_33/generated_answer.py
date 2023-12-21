
def if_decimal_is_divisible(bin_str):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_num = int(bin_str, 2)
    divisor = fibonacci(134)

    if decimal_num % divisor == 0:
        return True
    else:
        return False
