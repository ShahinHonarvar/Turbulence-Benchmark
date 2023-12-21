
def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fibonacci_num = [0, 1, 1, 2, 3, 5, 8]
    if decimal % fibonacci_num[6] == 0:
        return True
    else:
        return False
