
def if_decimal_is_divisible(binary_string):
    fibonacci_seq = [0, 1]
    while fibonacci_seq[-1] < 10**99:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fibonacci_seq[99] == 0
