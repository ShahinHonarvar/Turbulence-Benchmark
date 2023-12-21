
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fib_sequence = [0, 1]
    for _ in range(2, 119):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return num % fib_sequence[-1] == 0
