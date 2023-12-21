
def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    while len(fib_numbers) < 131:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        
    decimal = int(binary_str, 2)
    
    if decimal % fib_numbers[130] == 0:
        return True
    else:
        return False
