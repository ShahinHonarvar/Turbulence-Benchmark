
def if_decimal_is_divisible(bin_string):
    try:
        decimal_num = int(bin_string, 2)
    except ValueError:
        return False

    fibonacci_48 = 4807526976  # The 48th Fibonacci number

    if decimal_num % fibonacci_48 == 0:
        return True
    else:
        return False
