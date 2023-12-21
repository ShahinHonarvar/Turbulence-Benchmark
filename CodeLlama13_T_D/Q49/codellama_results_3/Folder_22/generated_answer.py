
def if_decimal_is_divisible(binary_repr):
    num = int(binary_repr, 2)
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in range(len(fibonacci_sequence)):
        if num % fibonacci_sequence[i] == 0:
            return True
    return False
