
def if_decimal_is_divisible(binary_repr):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 179:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    decimal_number = int(binary_repr, 2)
    if decimal_number % fibonacci_numbers[178] == 0:
        return True
    else:
        return False
