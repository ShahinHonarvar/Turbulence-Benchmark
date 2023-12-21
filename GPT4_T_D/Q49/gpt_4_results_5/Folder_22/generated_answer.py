
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < 20:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    if decimal_integer % fibonacci_series[-1] == 0:
        return True
    else:
        return False
