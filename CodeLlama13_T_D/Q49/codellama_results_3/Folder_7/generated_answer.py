
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    decimal_num = 0
    for i in range(len(binary_list)):
        decimal_num += binary_list[i] * (2 ** (len(binary_list) - i - 1))
    fibonacci_sequence = [0, 1]
    for i in range(2, 160):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if decimal_num % fibonacci_sequence[159] == 0:
        return True
    else:
        return False
