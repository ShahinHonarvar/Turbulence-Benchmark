
def if_decimal_is_divisible(binary_string):

    def nth_fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
      
    decimal_integer = int(binary_string, 2)
    fib_120th = nth_fibonacci(120)

    return decimal_integer % fib_120th == 0
