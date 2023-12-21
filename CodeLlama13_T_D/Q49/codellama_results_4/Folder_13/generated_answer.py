
def if_decimal_is_divisible(binary_string):
    binary_list = list(reversed(binary_string))
    fibonacci_sequence = [0, 1]
    for i in range(2, len(binary_list)):
        fibonacci_sequence.append((fibonacci_sequence[i-1] + fibonacci_sequence[i-2]) % 174)
    decimal = 0
    for i in range(len(binary_list)):
        decimal += (int(binary_list[i]) * fibonacci_sequence[i])
    return bool(decimal % 174 == 0)
