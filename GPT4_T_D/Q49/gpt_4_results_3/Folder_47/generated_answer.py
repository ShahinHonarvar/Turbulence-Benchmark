
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_sequence = [0, 1]

    for i in range(2, 94):
        next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_number)

    return decimal_integer % fibonacci_sequence[-1] == 0
