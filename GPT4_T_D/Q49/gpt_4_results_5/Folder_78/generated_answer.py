
def if_decimal_is_divisible(bin_str):
    def get_fib_seq(n):
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    aim_fib_num = get_fib_seq(116)[-1]
    decimal_num = int(bin_str, 2)
    if decimal_num % aim_fib_num == 0:
        return True
    else:
        return False
