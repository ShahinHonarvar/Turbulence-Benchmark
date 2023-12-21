
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_number = [0, 1]
    for _ in range(116):
        fibonacci_number.append(fibonacci_number[-1] + fibonacci_number[-2])
    if decimal_number % fibonacci_number[-1] == 0:
        return True
    else:
        return False
