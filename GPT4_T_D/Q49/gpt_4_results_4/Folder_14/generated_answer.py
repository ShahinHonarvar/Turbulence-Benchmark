
def if_decimal_is_divisible(binary_string):
    number = int(binary_string, 2)
    fibonacci_27th = 196418
    return number % fibonacci_27th == 0
