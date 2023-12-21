
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_nums = [0, 1]
    for _ in range(78):
        fib_nums.extend([fib_nums[-1] + fib_nums[-2]])
    if decimal_number % fib_nums[-1] == 0:
        return True
    else:
        return False
