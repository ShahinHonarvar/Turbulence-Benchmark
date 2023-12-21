
def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)

    fibonacci_list = [0, 1]
    while len(fibonacci_list) < 64:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        
    if decimal % fibonacci_list[-1] == 0:
        return True
    else:
        return False
