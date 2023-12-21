
def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    for i in range(2, 159):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal_value % fibonacci_sequence[-1] == 0
