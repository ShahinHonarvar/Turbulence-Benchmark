
def if_decimal_is_divisible(bin_str):
    num = int(bin_str, 2)

    fib_sequence = [0, 1]
    for i in range(2, 64):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return num % fib_sequence[-1] == 0
