
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_sequence = [0, 1]
    for i in range(2, 176):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    if decimal_number % fib_sequence[175] == 0:
        return True
    else:
        return False
