
def if_decimal_is_divisible(binary_decimal):
    fibonacci_sequence = [0, 1]
    a, b = 0, 1
    
    while len(str(fibonacci_sequence[-1])) < 125:
        a, b = b, a + b
        fibonacci_sequence.append(b)

    decimal = int(binary_decimal, 2)
    
    return decimal % fibonacci_sequence[124] == 0
