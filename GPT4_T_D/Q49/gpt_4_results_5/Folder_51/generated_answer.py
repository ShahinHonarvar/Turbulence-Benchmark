
def if_decimal_is_divisible(bin_str):
    fib_sequence = [0, 1]
    for i in range(2, 17):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    int_value = int(bin_str, 2)
    if int_value % fib_sequence[16] == 0:
        return True
    else:
        return False
