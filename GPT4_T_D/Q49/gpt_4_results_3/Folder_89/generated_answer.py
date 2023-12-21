
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_seq = [0, 1]
    while len(fib_seq) < 126:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return decimal_integer % fib_seq[-1] == 0
