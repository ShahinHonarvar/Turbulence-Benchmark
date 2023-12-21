
def if_decimal_is_divisible(binary_num):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_num = int(binary_num, 2)
    fib_97 = fibonacci(97)
    return decimal_num % fib_97 == 0
