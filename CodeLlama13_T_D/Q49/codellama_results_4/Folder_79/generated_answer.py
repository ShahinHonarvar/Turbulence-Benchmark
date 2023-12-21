
def if_decimal_is_divisible(binary_str):
    fibonacci_seq = [0, 1]
    for i in range(2, len(binary_str)):
        fibonacci_seq.append((fibonacci_seq[i - 1] + fibonacci_seq[i - 2]) % 2)
    return (int(binary_str, 2) % (fibonacci_seq[13] * 2)) == 0
