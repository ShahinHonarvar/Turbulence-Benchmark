
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    decimal = int(binary_string, 2)
    return fibonacci_sequence[144] in str(decimal)
