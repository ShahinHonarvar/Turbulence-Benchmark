
def if_decimal_is_divisible(decimal):
    fibonacci_sequence = [0, 1]
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
        if len(fibonacci_sequence) == 115:
            break
    decimal_integer = int(decimal, 2)
    return decimal_integer % fibonacci_sequence[114] == 0
