
def if_decimal_is_divisible(binary_str):
    fibonacci_numbers = [0,1]
    num = int(binary_str,2)
    while len(fibonacci_numbers) < 118:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return num % fibonacci_numbers[-1] == 0
