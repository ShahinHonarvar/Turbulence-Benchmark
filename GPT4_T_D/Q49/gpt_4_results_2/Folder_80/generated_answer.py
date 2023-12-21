
def if_decimal_is_divisible(binary_string):
    sequence = [0, 1]
    for i in range(2, 179):
        sequence.append(sequence[i - 1] + sequence[i - 2])
        
    decimal_number = int(binary_string, 2)

    return decimal_number % sequence[178] == 0
