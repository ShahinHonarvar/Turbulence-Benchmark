
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_series = [0, 1]
    for _ in range(2, 170):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return decimal_integer % fib_series[-1] == 0
