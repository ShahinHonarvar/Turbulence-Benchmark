
def if_decimal_is_divisible(bin_str):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    num = int(bin_str, 2)
    target = fibonacci(186)
    return num % target == 0
