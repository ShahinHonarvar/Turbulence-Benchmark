
def if_decimal_is_divisible(num):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 115:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    decimal_num = int(num, 2)
    return decimal_num % fib_sequence[114] == 0
