
def if_decimal_is_divisible(binary_string):
    fibonacci_numbers = [0, 1]
    for _ in range(2, 97):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
        
    decimal_number = int(binary_string, 2)
    
    if decimal_number % fibonacci_numbers[-1] == 0:
        return True
    else:
        return False
