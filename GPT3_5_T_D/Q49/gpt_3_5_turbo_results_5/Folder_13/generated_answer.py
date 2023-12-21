
def if_decimal_is_divisible(binary_representation):
    Fibonacci_sequence = [0, 1]
    while len(Fibonacci_sequence) <= 174:
        Fibonacci_sequence.append(Fibonacci_sequence[-1] + Fibonacci_sequence[-2])
    decimal_integer = int(binary_representation, 2)
    if decimal_integer % Fibonacci_sequence[173] == 0:
        return True
    else:
        return False
