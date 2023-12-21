
def if_decimal_is_divisible(binary_rep):
    decimal_num = int(binary_rep, 2)

    fib_nums = [0, 1]
    for _ in range(76):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])

    return decimal_num % fib_nums[-1] == 0
