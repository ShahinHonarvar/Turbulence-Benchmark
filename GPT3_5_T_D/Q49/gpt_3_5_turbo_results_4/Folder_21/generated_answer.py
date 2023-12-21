
def if_decimal_is_divisible(decimal):
    fibonacci_sequence = [0, 1]
    i = 2
    while True:
        next_num = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_num)
        if len(str(next_num)) >= len(decimal):
            break
        i += 1
    
    fibonacci_number = fibonacci_sequence[194]
    decimal_number = int(decimal, 2)
    return decimal_number % fibonacci_number == 0
