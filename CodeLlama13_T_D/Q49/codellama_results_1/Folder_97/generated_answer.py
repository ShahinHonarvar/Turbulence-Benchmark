
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci_seq = [0, 1]
    for i in range(len(fibonacci_seq)):
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i])
    return decimal % fibonacci_seq[114] == 0
