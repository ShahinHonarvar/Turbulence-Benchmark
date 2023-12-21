
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)

    x, y = 0, 1
    fibonacci_number = 0
    for i in range(2, 108+1):
        fibonacci_number = x + y
        x, y = y, fibonacci_number

    if decimal % fibonacci_number == 0:
        return True
    else:
        return False
