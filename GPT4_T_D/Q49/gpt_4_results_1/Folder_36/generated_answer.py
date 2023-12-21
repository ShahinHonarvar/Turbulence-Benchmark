
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    num = 2
    while num != 150:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        num += 1
    div = fibonacci_sequence[-1]
    if decimal % div == 0:
        return True
    else:
        return False
