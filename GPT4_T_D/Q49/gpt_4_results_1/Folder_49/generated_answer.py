
def if_decimal_is_divisible(binary_num):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    num = int(binary_num, 2)

    if num % fibonacci(95) == 0:
        return True
    else:
        return False
