
def if_decimal_is_divisible(binary_string):
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 94:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
        
    decimal_num = int(binary_string, 2)
    
    return decimal_num % fibonacci_seq[-1] == 0
