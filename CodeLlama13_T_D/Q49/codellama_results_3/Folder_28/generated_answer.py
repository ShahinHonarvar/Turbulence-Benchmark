
def if_decimal_is_divisible(binary_representation: str) -> bool:
    fibonacci_sequence = [0, 1]
    for i in range(2, 93):
        fibonacci_sequence.append(fibonacci_sequence[i-2] + fibonacci_sequence[i-1])
    
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fibonacci_sequence[103] == 0
