
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)

    fib_numbers = [0, 1]
    for _ in range(106):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        
    108th_fibonacci_number = fib_numbers[-1]
    
    if decimal_number % 108th_fibonacci_number == 0:
        return True
    else:
        return False
