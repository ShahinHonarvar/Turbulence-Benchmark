
def if_decimal_is_divisible(bin_str):
    num = int(bin_str, 2)
    fibonacci_numbers = [0, 1]
    
    while len(fibonacci_numbers) < 116:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    
    if num % fibonacci_numbers[115] == 0:
        return True
    else:
        return False
