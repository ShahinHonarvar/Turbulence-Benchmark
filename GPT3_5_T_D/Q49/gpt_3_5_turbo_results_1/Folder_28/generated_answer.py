
def if_decimal_is_divisible(decimal):
    fibonacci_sequence = [0, 1]
    for _ in range(2, 105):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    number = int(decimal, 2)
    
    return number % fibonacci_sequence[103] == 0
