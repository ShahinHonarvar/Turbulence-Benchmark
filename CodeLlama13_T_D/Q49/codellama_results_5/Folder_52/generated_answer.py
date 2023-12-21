
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    fibonacci_sequence = [0, 1]
    for i in range(2, len(binary_list)):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    if sum(binary_list[::-1][:len(fibonacci_sequence)]) % fibonacci_sequence[-1] == 0:
        return True
    else:
        return False
