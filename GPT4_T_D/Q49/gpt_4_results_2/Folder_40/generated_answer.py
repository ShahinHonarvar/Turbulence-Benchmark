
def if_decimal_is_divisible(binary_string):
    decimal_rep = int(binary_string, 2)
    fibonacci_numbers = [0, 1, 1]
    
    while len(fibonacci_numbers) < 4:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
        
    fourth_fibonacci = fibonacci_numbers[3]
    
    if decimal_rep % fourth_fibonacci == 0:
        return True
    else:
        return False
