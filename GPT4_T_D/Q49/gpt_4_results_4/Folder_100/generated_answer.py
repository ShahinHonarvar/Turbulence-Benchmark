
def if_decimal_is_divisible(binary_string):
    fibonacci_numbers = [0, 1]
    for i in range(2, 190):
        fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
    decimal = int(binary_string, 2)
    return decimal % fibonacci_numbers[-1] == 0
