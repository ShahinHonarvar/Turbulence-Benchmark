
def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    decimal_num = int(binary_str, 2)
    for i in range(len(fibonacci_sequence)):
        if fibonacci_sequence[i] == 14:
            return True
        elif fibonacci_sequence[i] > decimal_num:
            return False
    return False
