
def if_decimal_is_divisible(binary_string):
    bin_num = int(binary_string, 2)
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    fib_47 = fibonacci(47)
    if bin_num % fib_47 == 0:
        return True
    else:
        return False
