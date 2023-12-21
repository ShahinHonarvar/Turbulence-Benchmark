
def if_decimal_is_divisible(binary_string):
    binary_int = int(binary_string, 2)
    fibonacci_number = [0, 1]
    while len(fibonacci_number) <= 114:
        fibonacci_number.append(fibonacci_number[-2] + fibonacci_number[-1])
    if binary_int % fibonacci_number[114] == 0:
        return True
    else:
        return False
