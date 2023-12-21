
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_seq = [0, 1]
    for i in range(2, len(fibonacci_seq)):
        fibonacci_seq.append(fibonacci_seq[i-2] + fibonacci_seq[i-1])
    return decimal % fibonacci_seq[134] == 0
