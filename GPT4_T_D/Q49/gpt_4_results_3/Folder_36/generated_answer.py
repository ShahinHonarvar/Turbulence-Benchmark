
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)

    fib_nums = [0, 1]
    for _ in range(148):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])

    if decimal_integer % fib_nums[-1] == 0:
        return True
    else:
        return False
