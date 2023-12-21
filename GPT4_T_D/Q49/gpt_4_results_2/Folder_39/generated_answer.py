
def if_decimal_is_divisible(binary_string):
    fib_sequence, fib_1, fib_2 = [0, 1], 0, 1
    for _ in range(13):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        fib_sequence.append(fib_2)
        
    decimal_number = int(binary_string, 2)
    if decimal_number % fib_sequence[14] == 0:
        return True
    return False
