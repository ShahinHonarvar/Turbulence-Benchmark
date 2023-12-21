
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= 195:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    divisible_num = fibonacci_sequence[-1]
    decimal_number = int(binary_representation, 2)
    if decimal_number % divisible_num == 0:
        return True
    else:
        return False
