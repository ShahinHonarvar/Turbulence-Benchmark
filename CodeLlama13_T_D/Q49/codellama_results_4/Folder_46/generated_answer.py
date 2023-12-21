
def if_decimal_is_divisible(binary_string):
    binary_list = list(map(int, binary_string))
    fibonacci_sequence = [0]
    current = 1
    while True:
        fibonacci_sequence.append(current)
        if len(fibonacci_sequence) == 139:
            break
        current += fibonacci_sequence[-2]
    decimal_number = sum(binary_list[i] * fibonacci_sequence[i] for i in range(len(binary_list)))
    return decimal_number % fibonacci_sequence[138] == 0
