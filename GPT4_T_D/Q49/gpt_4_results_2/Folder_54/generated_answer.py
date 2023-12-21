
def if_decimal_is_divisible(binary_string):
    binary_to_decimal = int(binary_string, 2)
    fib_seq = [0, 1]
    for i in range(2, 34):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    if binary_to_decimal % fib_seq[-1] == 0:
        return True
    else:
        return False
