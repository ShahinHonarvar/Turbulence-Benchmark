
def if_decimal_is_divisible(binary):
    fibonacci_numbers = [0, 1]
    n = 2
    while n < 166:
        fibonacci_numbers.append(fibonacci_numbers[n - 1] + fibonacci_numbers[n - 2])
        n += 1

    decimal = int(binary, 2)
    return decimal % fibonacci_numbers[-1] == 0
