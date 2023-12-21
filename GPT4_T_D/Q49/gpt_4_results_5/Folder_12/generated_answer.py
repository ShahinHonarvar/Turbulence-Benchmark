
def if_decimal_is_divisible(binary):
    fibonacci_sequence = [0, 1]
    for i in range(2, 66):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    decimal = int(binary, 2)

    return decimal % fibonacci_sequence[65] == 0
