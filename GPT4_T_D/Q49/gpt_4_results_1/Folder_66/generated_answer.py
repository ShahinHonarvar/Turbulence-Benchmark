
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_numbers = [0, 1]
    for _ in range(2, 120):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    120th_fibonacci_number = fibonacci_numbers[-1]
    return decimal_integer % 120th_fibonacci_number == 0
