
def if_decimal_is_divisible(binary):
    sequence = [0, 1]
    while len(sequence) < 128:
        sequence.append(sequence[-1] + sequence[-2])
    decimal = int(binary, 2)
    if decimal % sequence[127] == 0:
        return True
    else:
        return False
