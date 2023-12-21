
def if_decimal_is_divisible(binary_string):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < 78:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    number = int(binary_string, 2)
    return number % fibonacci_numbers[77] == 0
