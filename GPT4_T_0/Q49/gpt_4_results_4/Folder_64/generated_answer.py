
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 10:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    tenth_fibonacci_number = fibonacci_sequence[-1]
    return decimal_number % tenth_fibonacci_number == 0
