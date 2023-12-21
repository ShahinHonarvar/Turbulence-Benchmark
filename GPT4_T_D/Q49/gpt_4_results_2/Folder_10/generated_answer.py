
def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0,1]

    while(len(fibonacci_sequence) < 88):
        val = fibonacci_sequence[-2] + fibonacci_sequence[-1]
        fibonacci_sequence.append(val)

    decimal_equivalent = int(binary_str, 2)

    return decimal_equivalent % fibonacci_sequence[87] == 0
