
def if_decimal_is_divisible(binary_string):
    fibonacci_numbers = [0, 1]
    i = 2
    while len(fibonacci_numbers) < 115:
        fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
        i += 1
    number = int(binary_string, 2)
    return number % fibonacci_numbers[114] == 0
