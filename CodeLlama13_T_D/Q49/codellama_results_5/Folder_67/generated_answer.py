
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    fibonacci_sequence = [0, 1]
    for i in range(2, len(binary_list)):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if sum(map(lambda x: x * fibonacci_sequence[i], enumerate(binary_list))) % fibonacci_sequence[107]:
        return True
    else:
        return False
