
def if_decimal_is_divisible(binary):
    fibonacci_sequence = [0, 1]
    for next_num in range(2, 35):
        fibonacci_sequence.append(fibonacci_sequence[next_num-1] + fibonacci_sequence[next_num-2])
    decimal = int(binary, 2)
    if decimal % fibonacci_sequence[-1] == 0:
        return True
    else:
        return False
