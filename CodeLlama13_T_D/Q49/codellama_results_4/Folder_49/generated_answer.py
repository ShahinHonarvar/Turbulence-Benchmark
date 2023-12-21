
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    fibonacci_sequence = []
    current = 0
    for i in range(len(binary_list)):
        next = current + binary_list[i] * (2 ** i)
        if next > 0:
            fibonacci_sequence.append(next)
            current = next
    return fibonacci_sequence[94] % fibonacci_sequence[95] == 0
