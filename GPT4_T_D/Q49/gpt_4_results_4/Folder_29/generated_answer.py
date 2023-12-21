
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    first, second = 0, 1
    for index in range(116):
        third = first + second
        first = second
        second = third
    if decimal_integer % third == 0:
        return True
    else:
        return False
