
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_seq = [0, 1]
    for i in range(len(binary_string)):
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i])
    return decimal % fibonacci_seq[97] == 0
