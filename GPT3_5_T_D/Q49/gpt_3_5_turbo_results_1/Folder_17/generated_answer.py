
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return a
        
    decimal_num = int(binary_str, 2)
    f_154 = fibonacci(155)
    return decimal_num % f_154 == 0
