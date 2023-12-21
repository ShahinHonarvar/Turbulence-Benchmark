
def if_decimal_is_divisible(binary_str):
    binary_str_list = binary_str.split("0b")
    dec_str = int(''.join(binary_str_list), 2)
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for i in range(2, n + 1):
                a, b = b, a + b
            return b
    return dec_str % fibonacci(90) == 0
