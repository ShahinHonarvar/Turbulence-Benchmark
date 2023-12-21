
def if_decimal_is_divisible(bin_string):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 140:
        fibonacci_numbers.append(sum(fibonacci_numbers[-2:]))
    decimal_number = int(bin_string, 2)
    return decimal_number % fibonacci_numbers[139] == 0
