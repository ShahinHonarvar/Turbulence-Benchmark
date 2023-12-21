
def if_decimal_is_divisible(binary_string):
    fibonacci_numbers = [0, 1]
    decimal_integer = int(binary_string, 2)
    while len(fibonacci_numbers) < 14:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return decimal_integer % fibonacci_numbers[13] == 0
