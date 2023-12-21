
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    i = 2
    while i < 160:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        i += 1
    decimal_integer = int(binary_string, 2)
    if decimal_integer % fibonacci_sequence[-1] == 0:
        return True
    else:
        return False
