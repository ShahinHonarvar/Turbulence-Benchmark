
def if_decimal_is_divisible(binary_string):
    def get_fibonacci(n):
        fib_values = [0, 1]
        while len(fib_values) < n:
            fib_values.append(fib_values[-1] + fib_values[-2])
        return fib_values[-1]

    number_179_in_fibonacci = get_fibonacci(180)
    decimal_integer = int(binary_string, 2)
    return decimal_integer % number_179_in_fibonacci == 0
