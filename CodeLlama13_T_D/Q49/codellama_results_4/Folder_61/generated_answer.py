
def if_decimal_is_divisible(binary_str):
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) <= binary_str.count('1'):
        fibonacci_seq.append(fibonacci_seq[-2] + fibonacci_seq[-1])
    
    decimal = int(binary_str, 2)
    return (decimal % fibonacci_seq[binary_str.count('1')]) == 0
