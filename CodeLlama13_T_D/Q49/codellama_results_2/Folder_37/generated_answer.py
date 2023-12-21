
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    decimal = 0
    for i in range(len(binary_list)):
        decimal += binary_list[i] * (2 ** i)
    fibonacci_sequence = [0, 1]
    for i in range(2, len(fibonacci_sequence)):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if decimal % fibonacci_sequence[45] == 0:
        return True
    else:
        return False
