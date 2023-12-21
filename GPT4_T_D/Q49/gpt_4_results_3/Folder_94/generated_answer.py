
def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 41:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    if decimal_integer % fibonacci_numbers[-1] == 0:
        return True
    else:
        return False
