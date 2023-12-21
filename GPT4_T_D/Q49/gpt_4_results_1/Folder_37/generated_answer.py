
def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_list = [0, 1]
    for i in range(2, 46):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        
    if decimal_number % fibonacci_list[-1] == 0:
        return True
    else:
        return False
