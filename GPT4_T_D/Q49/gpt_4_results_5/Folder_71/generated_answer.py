
def if_decimal_is_divisible(binary_string):
    def calculate_fib(num):
        a, b = 0, 1
        for _ in range(num):
            a, b = b, a + b
        return a

    fib_147 = calculate_fib(147)
    decimal_num = int(binary_string, 2)

    return decimal_num % fib_147 == 0
