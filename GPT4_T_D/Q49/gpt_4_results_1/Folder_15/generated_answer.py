
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < 9:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    if decimal % fibonacci_list[8] == 0:
        return True
    else:
        return False
