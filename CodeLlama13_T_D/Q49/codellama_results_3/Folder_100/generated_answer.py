
def if_decimal_is_divisible(binary_repr):
    binary_repr = binary_repr[::-1]  # Reverse the string
    decimal_value = int(binary_repr, 2)  # Convert to decimal
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) <= 190:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return decimal_value % fibonacci_seq[190] == 0
