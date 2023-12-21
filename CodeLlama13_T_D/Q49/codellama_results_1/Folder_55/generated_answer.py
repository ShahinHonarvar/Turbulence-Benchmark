
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    decimal_num = 0
    for i in range(len(binary_list)):
        decimal_num += binary_list[i] * (2 ** (len(binary_list) - 1 - i))
    fibonacci_seq = [0, 1]
    for i in range(2, len(fibonacci_seq)):
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i-2])
    if decimal_num % fibonacci_seq[39] == 0:
        return True
    else:
        return False
