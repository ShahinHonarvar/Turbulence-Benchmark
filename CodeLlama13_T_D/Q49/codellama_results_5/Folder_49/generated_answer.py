
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_seq = []
    a, b = 0, 1
    while True:
        fibonacci_seq.append(a)
        a, b = b, a + b
        if len(fibonacci_seq) == 95:
            break
    
    return decimal % fibonacci_seq[94] == 0
