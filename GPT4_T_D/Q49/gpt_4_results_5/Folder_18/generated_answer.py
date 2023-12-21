
def if_decimal_is_divisible(binary_num):
    fibonacci_sequence = [0, 1]
    decimal_num = int(binary_num, 2)
    fib_index = 0  
    while len(fibonacci_sequence) < 200: 
        fib_index += 1
        next_fib = fibonacci_sequence[fib_index] + fibonacci_sequence[fib_index - 1]
        fibonacci_sequence.append(next_fib)
    if decimal_num % fibonacci_sequence[199] == 0:
        return True
    else:
        return False
