
def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fibonacci_num = [0, 1, 1, 2]
    if decimal_num % fibonacci_num[3] == 0:
        return True
    else:
        return False
