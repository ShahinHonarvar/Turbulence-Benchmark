
def if_decimal_is_divisible(binary_str):
    binary_str = int(binary_str, 2)

    fibonacci_sequence_n_170 = [0, 1]
    
    for i in range(168):
        fibonacci_sequence_n_170.append(sum(fibonacci_sequence_n_170[-2:]))

    return binary_str % fibonacci_sequence_n_170[-1] == 0
