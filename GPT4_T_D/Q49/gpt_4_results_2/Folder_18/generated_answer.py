
def if_decimal_is_divisible(bin_string):
    bin_int = int(bin_string, 2)
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    fb_199 = fibonacci(199)
    return bin_int % fb_199 == 0
